###############################################################################
# python_liste_general.py
# Considerăm o listă dată l.
# 1. Să se scrie o funcție care citește un cuvînt de la tastatură
# și, dacă acesta există în listă, e șters din poziția curentă și
# mutat la final, iar dacă nu există, este adăugat la final.
# 2. Scrieți o secvență de cod care să înlocuiască toate elementele
# de tip șir conținînd mai multe nume de flori separate prin virgulă,
# punînd în loc numele de flori ca elemente și eliminînd spațiile în
# plus. Lista rezultată va fi pusă în variabila inițială și se va afișa.
# 3. Să se scrie o funcție care primește un caracter și lista de cuvinte
# l și se returnează o listă nouă doar cu cuvintele ce conțin acel caracter.
# 4. Să se sorteze și afișeze lista de cuvinte în ordine alfabetică și
# invers alfabetică. Folosiți sort și reverse.
###############################################################################

flori = ["margareta", "crizantema", "lalea", "zorea, violeta, orhidee",
         "trandafir", "gerbera, iasomie", "iris", "crin "]

cuvint = str(input("Introduceți cuvîntul de căutat: "))


def adSt(cuvint):
    for i in range(0, len(flori)-1):
        if flori[i] == cuvint:
            del flori[i]
    flori.append(cuvint)
    print(flori)


adSt(cuvint)
print("##################################################")


flori = [elem.split(", ") for elem in flori]


def flatten(lst):
    return [item for sublist in lst for item in sublist]


flori = flatten(flori)
print(flori)
print("##################################################")

caracter = str(input("Introduceți caracterul: "))
print("Cuvintele din lista care conțin acel caracter sînt: ")


def areCaracter(car, lst):
    cuCaracter = []
    for floare in lst:
        if caracter in floare:
            cuCaracter.append(floare)
    return cuCaracter


print(areCaracter(caracter, flori))
print("##################################################")

print("Lista sortată și inversată:")
flori.sort(key=str.lower)
print(flori)
flori.reverse()
print(flori)
print("=====PROGRAM TERMINAT=====")
