from elements_list import atom_masses


def flags(user_input):
    """
    This void function need if user use flags in commands.

    :param user_input:
    :return: Nothing
    """
    if '-h' in user_input:
        print("""
    _____Help Page_____

    To calculate molar mass just print compound without flags (note that register are import!)
        for example: (NH4)2Cr2O7    ->      252.061
                     h2o            ->      error
                ----------------------------
    [-i]                 show information about element (not compound!)
                            for example: Hg -i -> Mercury is liquid metal
                ----------------------------
    [-mp]                show melting point of element (not compound!)
                            for example: Fe -mp -> Iron melt at 1812 degrees Kelvin or 1538.85 degrees Celsius
                ____________________________
    [-u] + [dK/dC/dF]    change unit system
                            for example: Cl -mp -u dK -> Chlorine melts at 172.2 degrees Kelvin
                ----------------------------
    [-h]                 show this message
                ----------------------------
    [exit]               close
            """)
    if '-u' in user_input:
        print('Now only Kelvin scale support')
    if '-i' in user_input:  # find flags in input text
        if user_input[:2] in atom_masses and user_input[2] == ' ':
            print(atom_masses[user_input[:2]][1])
        elif user_input[0] in atom_masses and user_input[1] == ' ':
            print(atom_masses[user_input[0]][1])
        else:
            print('This element does not exist!')
    elif '-mp' in user_input:
        if user_input[:2] in atom_masses and user_input[2] == ' ':
            print(f'{atom_masses[user_input[:2]][1]} melts at {atom_masses[user_input[:2]][2]} degrees Kelvin')
        elif user_input[0] in atom_masses and user_input[1] == ' ':
            print(f'{atom_masses[user_input[0]][1]} melts at {atom_masses[user_input[0]][2]} degrees Kelvin')
        else:
            print('This element does not exist!')
    else:
        print('Unknown flag. Use [-h] to get help.')


def molar_calc(without_brackets):
    """
    This function find molar mass of compound. Don't use if compound has brackets!
        for example: CaSO4 -> 136.137
            Ca(NO3)3 -> may cause error
    :param without_brackets:
    :return: molar mass
    """
    f_molar_mass = 0
    # Check if compound could be
    if not without_brackets[:1] in atom_masses and not without_brackets[:2] in atom_masses:
        print("This compound does not exist! ")
    else:
        for k, char in enumerate(without_brackets):
            # if element in compound consist of 2 letters (like Li, He, Fe etc.)
            if without_brackets[k:k + 2] in atom_masses:
                if without_brackets[k + 2:3 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(without_brackets[k + 2:k + 3]) * atom_masses[without_brackets[k:k + 2]][0]
                else:
                    f_molar_mass += atom_masses[without_brackets[k:k + 2]][0]
                continue
            elif char in atom_masses:  # if element in compound consist of 1 letter (like H, C, N, O etc.)
                if without_brackets[k + 1:k + 2] in list('123456789'):  # check if element has index
                    f_molar_mass += int(without_brackets[k + 1:k + 2]) * atom_masses[char][0]
                else:
                    f_molar_mass += atom_masses[char][0]
    return round(f_molar_mass, 3)  # return rounded to 3 digits molar mass of formatted compound


def separator(with_brackets):
    """
    This function separate compound to brackets part and un brackets part. Don't use if no brackets in compound!
        for example: Fe(NO3)3 -> ('Fe' , 'NO3', 3)
            NaCl -> cause error
    :param with_brackets:
    :return: out brackets part, brackets part, brackets coefficient
    """
    # find parentheses
    first_bracket, second_bracket = with_brackets.find('('), with_brackets.find(')')
    # check is coefficient does exist
    is_coef = len(with_brackets) > second_bracket + 1 and with_brackets[second_bracket + 1] in '123456789'
    # save bracket part
    brackets_part = with_brackets[first_bracket + 1:second_bracket]
    # search coefficient
    coefficient = with_brackets[second_bracket + 1] if is_coef else 1
    # search out bracket part
    out_brackets_part = with_brackets[:first_bracket] + with_brackets[second_bracket + 2:] if \
        is_coef else \
        with_brackets[:first_bracket] + with_brackets[second_bracket + 1:]
    return out_brackets_part, brackets_part, int(coefficient)


while True:
    compound = input('''
___Warning! [-mp] cause program crash!___
Print compound symbol or [-h] to get help: ''')  # get input compound

    if compound == 'exit':  # exit function
        break
    elif '-' in compound:  # call flags function
        flags(compound)
    elif '(' in compound and ')' in compound:  # if we have brackets in compound
        molar_mass = molar_calc(separator(compound)[0]) + molar_calc(separator(compound)[1]) * separator(compound)[2]
        print(f'Molar mass of {compound} is {molar_mass}')
    else:  # if we do not have brackets in compound
        print(f'Molar mass of {compound} is {molar_calc(compound)}')
