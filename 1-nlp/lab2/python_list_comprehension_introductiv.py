###############################################################################
# python_list_comprehension.introductiv.py
# a. Sa se genereze si afiseze lista numerelor impare intre 0 si 10
# b. Sa se genereze lista literelor in lowercase de la a la z
# c. Sa se scrie o functie care primeste ca parametru un numar n. Sa se
# genereze lista de forma 1,-2,3,-4,... pana la n(cu semnul corespunzator).
# d. Sa se scrie o functie care primeste ca parametru o lista de numere. Sa se
# returneze lista cu elementele impare.
# e. Sa se scrie o functie care primeste ca parametru o lista de numere. Sa se
# returneze lista cu elementele de pe pozitiile impare.
# f. Sa se scrie o functie care calculeaza pentru o lista de numere data, lista
# continand elementele care au aceeasi paritate cu pozitia pe care se afla.
# De exemplu, pentru lista [2,4,1,7,5,1,8,10], lista calculata va contine
# elementele: 2, 7, 1, 8.
# g. Sa se scrie o functie care primeste o lista si returneaza lista cu
# perechiile (tupluri) de elementele de pe pozitii vecine. De exemplu pentru
# lista [1,2,3] lista rezultata ar fi [(1,2),(2,3),(3,4)]
# h. Sa se scrie o functie care primeste ca parametru un numar n si genereaza
# cu ajutorul list comprehension o lista de n liste. In fiecare lista element
# vom avea siruri de forma "x*y=rez". Elementul x va avea drept valoare
# indicele listei-element iar y va varia intre 1 si n (sirurile fiind ordonate
# crescator). Practic se genereaza tabla inmultirii numerelor de la 1 la n.
# Sa se apeleze functia si sa se afiseze rezultatul.
# i. Sa se scrie un list comprehension prin care, pornind de la un sir dar,
# de exemplu, sir="abcde" sa se obtina intr-o lista toate sirurile formate
# luand n litere de la inceputul sirului si concatenandu-le la sfarsit, cu n
# de la 0 pana la lungime(sir)-1. Pentru sirul dat ca exemplu, lista de
# calculat ar fi: ['abcde', 'bcdea', 'cdeab', 'deabc', 'eabcd']
# j. Sa se scrie o functie care returneaza o lista de n liste (unde n e dat ca
# parametru in functie), cu proprietatea ca prima lista va fi vida, a doua
# lista va avea un singur element egal cu 1, a treia lista va avea doua
# elemente egale cu 2, si asa mai departe pana la a n-a lista care va avea
# n-1 elemente egale cu n-1. De exemplu pentru n=4, lista de liste va fi:
# [[],[1],[2,2],[3,3,3]]
###############################################################################

print("a. Numere impare 0..10: " + str([x for x in range(10) if x % 2 == 1]))

print("b. Litere lower: ")
print(str([chr(x) for x in range(127) if chr(x).islower()]))


def sirAlternat(nr):
    print([(-1) ** elt * (elt + 1) for elt in range(nr)])


print("c. Șir alternat: ")
sirAlternat(20)


def eltImpare(lista):
    print([elt for elt in lista if elt % 2 == 1])


print("d. Elementele impare: ")
eltImpare([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def eltPozImpare(lista):
    print([lista[x] for x in range(len(lista)) if x % 2 == 1])


print("e. Elementele de pe poziții impare: ")
eltPozImpare([12, 545, 67, 23, 11])


def listaParitati(lista):
    print([lista[x] for x in range(len(lista)) if x % 2 == lista[x] % 2])


print("f. Lista cu elementele de aceeași paritate cu poziția: ")
listaParitati([2, 4, 1, 7, 5, 1, 8, 10])


def tupluriVecine(lista):
    print([(lista[i], lista[i+1]) for i in range(len(lista) - 1)])


print("g. Lista de tupluri vecine: ")
tupluriVecine([1, 2, 3, 4])


def tablaInm(nr):
    print([[str(x) + "*" + str(y) + "=" + str(x*y) for x in range(1, nr)]
           for y in range(1, nr)])


print("h. Tabla înmulțirii: ")
tablaInm(5)


def concatSiruri(sir):
    print([sir[x:] + sir[:x] for x in range(len(sir))])


print("i. Subșiruri concatenate: ")
concatSiruri("abcde")


def listaDeListe(nr):
    print([[x] * x for x in range(nr)])


print("j. Lista de liste: ")
listaDeListe(5)
