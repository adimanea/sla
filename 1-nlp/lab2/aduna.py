###############################################################################
# python_argumente_program.py
# Sa se scrie un program aduna.py. Acesta va contine o functie aduna cu numar
# variabil de argumente, care returneaza suma lor. Programul aduna.py va primi
# ca argumente niste numere si, folosind functia mentionata anterior, va afisa
# suma numerelor. Daca unul dintre argumentele primite de program nu e numar,
# programul va afisa mesajul "Nu se poate face suma.".
###############################################################################

import sys


def aduna(*args):
    suma = 0
    for arg in args:
        for elt in arg:
            if not elt.isdigit():
                print("Nu se poate face suma.")
                sys.exit(0)
            suma += int(elt)
    print("Suma = " + str(suma))

aduna(sys.argv[1:])
