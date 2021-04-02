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


def molar_calc(formatted_compound):  # this function find molar mass of formatted compound without brackets
    f_molar_mass = 0
    # Check if compound could be
    if not formatted_compound[:1] in atom_masses and not formatted_compound[:2] in atom_masses:
        print("This compound does not exist! ")
    else:
        for k in range(len(formatted_compound)):
            # if element in compound consist of 2 letters (like Li, He, Fe etc.)
            if formatted_compound[k:2 + k] in atom_masses:
                if formatted_compound[k + 2:3 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(formatted_compound[k + 2:3 + k]) * atom_masses[formatted_compound[k:2 + k]][0]
                else:
                    f_molar_mass += atom_masses[formatted_compound[k:2 + k]][0]
                k += 1
            elif formatted_compound[
                 k:1 + k] in atom_masses:  # if element in compound consist of 1 letter (like H, C, N, O etc.)
                if formatted_compound[k + 1:2 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(formatted_compound[k + 1:2 + k]) * atom_masses[formatted_compound[k:1 + k]][0]
                else:
                    f_molar_mass += atom_masses[formatted_compound[k:1 + k]][0]
    return round(f_molar_mass, 3)  # return rounded to 3 digits molar mass of formatted compound


# this function separate input compound to in bracket piece and un bracket piece
def compound_separator(no_flags_input):
    out_brackets_piece = ''
    # find parentheses
    first_brackets_pos, second_brackets_pos = no_flags_input.find('('), no_flags_input.find(')')
    brackets_piece = no_flags_input[first_brackets_pos + 1:second_brackets_pos]
    if first_brackets_pos == 0:  # if brackets piece in front of compound like (NH4)2SO4
        out_brackets_piece = no_flags_input[second_brackets_pos + 2:]
    if second_brackets_pos == len(no_flags_input) - 2:  # if brackets piece in end of compound like Fe(NO3)3
        out_brackets_piece = no_flags_input[:first_brackets_pos]
    brackets_coif = no_flags_input[second_brackets_pos + 1]
    return out_brackets_piece, brackets_piece, brackets_coif


while True:
    compound = input("Print compound symbol or [-help] to get help: ")  # get input compound

    if compound == 'exit':  # exit function
        break
    elif '-' in compound:  # call flags function
        flags(compound);
    elif '(' in compound and ')' in compound:  # if we have brackets in compound
        print(f'Molar mass of {compound} is ')
    else:  # if we do not have brackets in compound
        print(f'Molar mass of {compound} is {molar_calc(compound)}')
