from elements_list import atom_masses


def molar_calc(f_compound):  # this function find molar mass of formatted compound without brackets
    f_molar_mass = 0
    if not f_compound[:1] in atom_masses and not f_compound[:2] in atom_masses:  # Check if compound could be
        print("This compound does not exist! ")
    else:
        for i in range(len(f_compound)):
            if f_compound[i:2 + i] in atom_masses:  # if element in compound consist of 2 letters (like Li, He, Fe etc.)
                if f_compound[i + 2:3 + i] in list('123456789'):  # check if element has index
                    f_molar_mass += int(f_compound[i + 2:3 + i]) * atom_masses[f_compound[i:2 + i]]
                else:
                    f_molar_mass += atom_masses[f_compound[i:2 + i]]
                i += 1
            elif f_compound[
                 i:1 + i] in atom_masses:  # if element in compound consist of 1 letter (like H, C, N, O etc.)
                if f_compound[i + 1:2 + i] in list('123456789'):  # check if element has index
                    f_molar_mass += int(f_compound[i + 1:2 + i]) * atom_masses[f_compound[i:1 + i]]
                else:
                    f_molar_mass += atom_masses[f_compound[i:1 + i]]
    return round(f_molar_mass, 3)  # return rounded to 3 digits molar mass of formatted compound


def compound_separator(in_compound):  # this function separate input compound to in bracket piece and un bracket piece
    out_brackets_piece = ''
    first_brackets_pos, second_brackets_pos = None, None
    for i in range(len(in_compound)):
        if in_compound[i] == '(':  # if find bracket save bracket position
            first_brackets_pos = i
        if in_compound[i] == ')':
            second_brackets_pos = i
    if first_brackets_pos is not None and second_brackets_pos is not None:
        if first_brackets_pos == 0:  # if brackets piece in front of compound like (NH4)2SO4
            out_brackets_piece = in_compound[second_brackets_pos + 2:]
        if second_brackets_pos == len(in_compound) - 2:  # if brackets piece in end of compound like Fe(NO3)3
            out_brackets_piece = in_compound[:first_brackets_pos]
        brackets_piece = in_compound[first_brackets_pos + 1:second_brackets_pos]
        brackets_coif = in_compound[second_brackets_pos + 1]
        return out_brackets_piece, brackets_piece, brackets_coif


while True:
    compound = input("Print compound symbol or \"exit\" to close: ")  # get input compound

    if compound == 'exit':  # exit function
        break
    for i in range(len(compound)):
        if compound[0] == '(' or compound[len(compound) - 2] == ')':  # if compound has brackets used separator function
            molar_mass = molar_calc(compound_separator(compound)[0]) + molar_calc(
                compound_separator(compound)[1]) * float(compound_separator(compound)[2])
        else:  # else use just calc function
            molar_mass = molar_calc(compound)
    print(f'Molar mass of {compound} is {molar_mass}')
