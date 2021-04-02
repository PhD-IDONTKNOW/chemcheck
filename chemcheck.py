from elements_list import atom_masses


def flags(user_in):
    if '-info' in user_in or '-i' in user_in:  # find flags in input text
        if user_in[:2] in atom_masses and user_in[2] == ' ':
            print(atom_masses[user_in[:2]][1])
        elif user_in[0] in atom_masses and user_in[1] == ' ':
            print(atom_masses[user_in[0]][1])
        else:
            print('This element does not exist!')
    elif '-melting_point' in user_in or '-mp' in user_in:
        print('Elements melting point was not add yet, but water melt at 0 degrees Celsius')
    elif '-help' in user_in or '-h' in user_in:
        print("""
    _____Help Page_____

    To calculate molar mass just print compound without flags (note that register are import!)
        for example: (NH4)2Cr2O7    ->      252.061
                     h2o            ->      error
                    ----------------------------
    [-info] or [-i]             show information about element (not compound!)
                                    for example: Hg -info -> Mercury is liquid metal
                    ----------------------------
    [-melting_point] or [-mp]   show melting point of element (not compound!)
                                    for example: Fe -mp -> Iron melt at 1812 degrees Kelvin or 1538.85 degrees Celsius
                    ----------------------------
    [-help] or [-h]             show this message
                    ----------------------------
    [exit]                      close
            """)
    else:
        print('Unknown flag. Use [-help] to get help.')


def molar_calc(no_brackets):  # this function find molar mass of formatted compound without brackets
    f_molar_mass = 0
    # Check if compound could be
    if not no_brackets[:1] in atom_masses and not no_brackets[:2] in atom_masses:
        print("This compound does not exist! ")
    else:
        for k in range(len(no_brackets)):
            # if element in compound consist of 2 letters (like Li, He, Fe etc.)
            if no_brackets[k:2 + k] in atom_masses:
                if no_brackets[k + 2:3 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(no_brackets[k + 2:3 + k]) * atom_masses[no_brackets[k:2 + k]][0]
                else:
                    f_molar_mass += atom_masses[no_brackets[k:2 + k]][0]
                k += 1
            elif no_brackets[
                 k:1 + k] in atom_masses:  # if element in compound consist of 1 letter (like H, C, N, O etc.)
                if no_brackets[k + 1:2 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(no_brackets[k + 1:2 + k]) * atom_masses[no_brackets[k:1 + k]][0]
                else:
                    f_molar_mass += atom_masses[no_brackets[k:1 + k]][0]
    return round(f_molar_mass, 3)  # return rounded to 3 digits molar mass of formatted compound


# this function separate input compound to bracket part and un bracket part
def separator(no_flags):
    # find parentheses
    first_bracket, second_bracket = no_flags.find('('), no_flags.find(')')
    # check is coefficient does exist
    is_coef = len(no_flags) > second_bracket + 1 and no_flags[second_bracket + 1] in '123456789'
    # save bracket part
    brackets_part = no_flags[first_bracket + 1:second_bracket]
    # search coefficient
    coefficient = no_flags[second_bracket + 1] if is_coef else 1
    # search out bracket part
    out_brackets_part = no_flags[:first_bracket] + no_flags[second_bracket + 2:] if \
        is_coef else \
        no_flags[:first_bracket] + no_flags[second_bracket + 1:]
    return out_brackets_part, brackets_part, int(coefficient)


while True:
    compound = input("Print compound symbol or [-help] to get help: ")  # get input compound

    if compound == 'exit':  # exit function
        break
    elif '-' in compound:  # call flags function
        flags(compound)
    elif '(' in compound and ')' in compound:  # if we have brackets in compound
        molar_mass = molar_calc(separator(compound)[0]) + molar_calc(separator(compound)[1]) * separator(compound)[2]
        print(f'Molar mass of {compound} is {molar_mass}')
    else:  # if we do not have brackets in compound
        print(f'Molar mass of {compound} is {molar_calc(compound)}')
