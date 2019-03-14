###############################################################################
# python_any_all.py
# Rezolvati urmatoarele subpuncte folosind comprehensions, si functiile any
# si all. Pentru toate subpunctele, functiile trebuie apelate.
#       1. Sa se scrie o functie care primeste ca parametri o lista de numere.
# Functia va returna True daca toate numerele din lista sunt intregi si
# pozitive. Functia va returna False in caz contrar.
#       2. Sa se scrie o functie care primeste ca parametru o lista de siruri.
# Functia va returna True daca exista cel putin un sir care incepe si se
# termina cu acelasi caracter. Functia va returna False in caz contrar.
#       3. Sa se scrie o functie care returneaza True daca o matrice e formata
# doar din zerouri, si False in caz contrar. Functia va primi matricea ca
# parametru.
#       4. Sa se scrie o functie care primeste ca parametri un sir si o lista
# de cuvinte. Functia va returna True daca cel putin un cuvant din lista se
# gaseste in sir. Functia va returna False in caz contrar.
###############################################################################


def intregPozitiv(numar):
    return (isinstance(numar, int) and numar >= 0)


def toateIntregiPozitive(lista):
    print(all({intregPozitiv(x) for x in lista}))


print("Toate întregi pozitive: ")
toateIntregiPozitive([1, 2, 3, 4])      # true
toateIntregiPozitive([1.2, 3, 4])       # false
toateIntregiPozitive([-1, 2, 3])        # false

###############################################################################


def celPutin1IncepeSiSeTermina(lista):
    print(any({(sir[0] == sir[-1]) for sir in lista}))


print("Cel puțin unul începe și se termină la fel: ")
celPutin1IncepeSiSeTermina(["abc", "def", "aba"])       # true
celPutin1IncepeSiSeTermina(["abc", "def"])              # false

###############################################################################


def matriceZerouri(mat):
    print(all({(x == 0) for linie in mat for x in linie}))


print("Matrice doar cu zerouri: ")
matriceZerouri([[0, 0], [0, 0]])                        # true
matriceZerouri([[1, 0], [0, 0]])                        # false

###############################################################################


def eInLista(sir, listaCuv):
    print(any({cuv in sir for cuv in listaCuv}))


print("Cel puțin un cuvînt e în listă: ")
eInLista("pisica, om", ["om", "cîine"])         # true
eInLista("pisica, om", ["porc", "copil"])       # false
