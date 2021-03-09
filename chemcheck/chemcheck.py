from elements_list import atom_masses

def molar_mass_calc(compound):
    molar_mass = 0
    if not compound[:1] in atom_masses and not compound[:2] in atom_masses: 
        print(("This compound does not exist! "))
    else:
        for i in range(len(compound)):
            if compound[i:2 + i] in atom_masses:
                if compound[i + 2:3 + i] in list('123456789'):
                    print(f"Atom mass of {int(compound[i + 2:3 + i])} {compound[i:2 + i]} is {int(compound[i + 2:3 + i]) * atom_masses[compound[i:2 + i]]}")
                    molar_mass += int(compound[i + 2:3 + i]) * atom_masses[compound[i:2 + i]]
                else:
                    print(f"Atom mass of {compound[i:2 + i]} is {atom_masses[compound[i:2 + i]]}")
                    molar_mass += atom_masses[compound[i:2 + i]]
                i += 1
            elif compound[i:1 + i] in atom_masses:
                if compound[i + 1:2 + i] in list('123456789'):
                    print(f"Atom mass of {int(compound[i + 1:2 + i])} {compound[i:1 + i]} is {int(compound[i + 1:2 + i]) * atom_masses[compound[i:1 + i]]}")
                    molar_mass += int(compound[i + 1:2 + i]) * atom_masses[compound[i:1 + i]]
                else:
                    print(f"Atom mass of {compound[i:1 + i]} is {atom_masses[compound[i:1 + i]]}")
                    molar_mass += atom_masses[compound[i:1 + i]]
    return round(molar_mass, 3)

while(True):
    compound = input("Print compound symbol or \"exit\" to close: ")

    if compound == 'exit': break

    print(f'Molar mass of {compound} is {molar_mass_calc(compound)}')

