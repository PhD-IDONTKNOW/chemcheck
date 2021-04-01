from elements_list import atom_masses


def molar_calc(f_compound):  # this function find molar mass of formatted compound without brackets
    f_molar_mass = 0
    if not f_compound[:1] in atom_masses and not f_compound[:2] in atom_masses:  # Check if compound could be
        print("This compound does not exist! ")
    else:
        for k in range(len(f_compound)):
            if f_compound[k:2 + k] in atom_masses:  # if element in compound consist of 2 letters (like Li, He, Fe etc.)
                if f_compound[k + 2:3 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(f_compound[k + 2:3 + k]) * atom_masses[f_compound[k:2 + k]][0]
                else:
                    f_molar_mass += atom_masses[f_compound[k:2 + k]][0]
                k += 1
            elif f_compound[
                 k:1 + k] in atom_masses:  # if element in compound consist of 1 letter (like H, C, N, O etc.)
                if f_compound[k + 1:2 + k] in list('123456789'):  # check if element has index
                    f_molar_mass += int(f_compound[k + 1:2 + k]) * atom_masses[f_compound[k:1 + k]][0]
                else:
                    f_molar_mass += atom_masses[f_compound[k:1 + k]][0]
    return round(f_molar_mass, 3)  # return rounded to 3 digits molar mass of formatted compound


def compound_separator(in_compound):  # this function separate input compound to in bracket piece and un bracket piece
    out_brackets_piece = ''
    first_brackets_pos, second_brackets_pos = None, None
    for j in range(len(in_compound)):
        if in_compound[j] == '(':  # if find bracket save bracket position
            first_brackets_pos = j
        if in_compound[j] == ')':
            second_brackets_pos = j
    if first_brackets_pos is not None and second_brackets_pos is not None:
        if first_brackets_pos == 0:  # if brackets piece in front of compound like (NH4)2SO4
            out_brackets_piece = in_compound[second_brackets_pos + 2:]
        if second_brackets_pos == len(in_compound) - 2:  # if brackets piece in end of compound like Fe(NO3)3
            out_brackets_piece = in_compound[:first_brackets_pos]
        brackets_piece = in_compound[first_brackets_pos + 1:second_brackets_pos]
        brackets_coif = in_compound[second_brackets_pos + 1]
        return out_brackets_piece, brackets_piece, brackets_coif


while True:
    compound = input("Print compound symbol or [-help] to get help: ")  # get input compound

    if compound == 'exit':  # exit function
        break

    if '-info' in compound or '-i' in compound:  # find flags in input text
        if compound[:2] in atom_masses:
            print(atom_masses[compound[:2]][1])
        elif compound[0] in atom_masses:
            print(atom_masses[compound[0]][1])
        else:
            print('This element does not exist!')
    elif '-melting_point' in compound or '-mp' in compound:
        print('Elements melting point was not add yet, but water melt at 0 degrees Celsius')
    elif '-help' in compound or '-h' in compound:
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
    # if compound has brackets used separator function
    elif compound[0] == '(' or compound[len(compound) - 2] == ')':
        molar_mass = molar_calc(compound_separator(compound)[0]) + molar_calc(
            compound_separator(compound)[1]) * float(compound_separator(compound)[2])
        print(f'Molar mass of {compound} is {molar_mass}')
    else:  # else use just calc function
        molar_mass = molar_calc(compound)
        print(f'Molar mass of {compound} is {molar_mass}')
