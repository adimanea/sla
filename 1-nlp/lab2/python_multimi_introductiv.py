###############################################################################
# Rezolvati folosind multimi.
# a. Sa se scrie o functie care verifica faptul ca o lista e formata doar
# din elemente egale. Codul functiei trebuie sa aiba doar un rand (o
# instructiune). Apelati functia si afisati rezultatul.
# b. Sa se scrie o functie care verifica faptul ca un sir dat ca parametru
# contine tot alfabetul (returneaza True in cazul in care sirul e format din
# toate literele din alfabet si False in caz contrar). Se considera litere in
# case diferit aceeasi litera. Codul functiei trebuie sa aiba doar un rand
# (o instructiune). Apelati functia si afisati rezultatul.
# c. Sa se scrie o functie care verifica faptul ca doua siruri date ca
# argumente sunt anagrame unul pentru celalalt (returneaza True in cazul
# in care sunt anagrame si False in caz contrar). Se considera litere
# in case diferit sunt litere diferite. Codul functiei trebuie sa aiba
# doar un rand (o instructiune). Apelati functia si afisati rezultatul.
# Se poate rezolva folosind multimi? Explicati.
# d. Sa se genereze multimea submultimilor pentru o multime data. Cum
# trebuie sa fie submultimile? Afisati rezultatul.
# e. Sa se genereze produsul cartezian pentru doua multimi date. Elementele
# din produsul cartezian trebuie sa fie tupluri. Afisati rezultatul.
###############################################################################

import string

litere = set(string.ascii_letters)


def elEgale(lista):
    """ Funcția verifică dacă lista e formată
    doar din elemente egale."""
    return len(set(lista)) == 1


print(elEgale([1, 1, 1]))


def areToate(lista):
    """ Funcția verifică dacă lista conține
    toate literele alfabetului """
    return len(litere - set(lista)) == 0


print(areToate(["a", "bc"]))


def anagrame(cuv1, cuv2):
    """ Funcția verifică dacă cuvintele sînt anagrame. """
    # Rezolvarea este cu mulțimi.
    return (set(cuv1) == set(cuv2))


print(anagrame("abc", "caB"))  # false


def lista_subm(lst):
    """ LISTA de submulțimi """
    subm = [[]]
    for x in lst:
        subm.extend([subset + [x] for subset in subm])
    return subm


# convertim în mulțime
def submultimi(mult):
    return frozenset(map(frozenset, lista_subm(list(mult))))
# mulțimile trebuie să fie frozen, pentru a putea fi elemente
# în alte mulțimi


print(submultimi(frozenset([1, 2, 3])))


def pCartezian(set1, set2):
    return [{el1, el2} for el1 in set1 for el2 in set2]


print(pCartezian(set(["a", "b"]), set(["c", "d"])))
