###############################################################################
# python_dict_comprehensions.py
# Rezolvati subpunctele urmatoare folosind dict comprehensions.
#       1. Sa se genereze un dictionar in care cheile (k) sunt numerele
# naturale, mai mici decat 10, impare si valorile sunt liste cu numerele
# de la 1 la k.
#       2. Sa se scrie o functie care primeste ca parametru o lista de siruri
# si calculeaza un dictionar in care cheile sunt caracterele care apar in
# siruri iar valorile sunt multimile cuvintelor din lista care contin
# litera-cheie.
#       Sa se apeleze functia si sa se afiseze rezultatul.
#       3. Sa se scrie o functie care primeste ca parametru o lista de tupluri
# de cate 2 numere intregi (t1, t2) si calculeaza un dictionar in care cheile
# sunt chiar tuplurile. Valoarea pentru fiecare cheie (t1,t2) reprezinta o
# lista cu numerele consecutive aflate intre t1 si t2. Numerele vor fi in
# ordine crescatoare daca t1<t2 si descrescatoare pentru t2>e;t1.
#       Sa se apeleze functia si sa se afiseze rezultatul.
###############################################################################

dictionar = {k: [x for x in range(1, k + 1)] for k in range(1, 11, 2)}
print("1. Dicționar cu comprehension:")
print(dictionar)


def dictDinSiruri(listaSiruri):
    caractere = set([sir[i] for sir in listaSiruri for i in range(len(sir))])
    dictionar = {k: [cuv for cuv in listaSiruri if k in cuv]
                 for k in caractere}
    print(dictionar)


print("2. Dicționar cu cuvinte care conțin caractere din listă: ")
dictDinSiruri(["abc", "bcda", "ffasf", "xyasd"])


def dictDinTupluri(listaTupluri):
    dictionar = {(t1, t2): list(range(t1, t2 + 1)) if t1 < t2
                 else list(range(t1, t2 - 1, -1))
                 for (t1, t2) in listaTupluri}
    print(dictionar)


print("3. Dicționar din tupluri: ")
dictDinTupluri([(1, 3), (7, 4), (3, 1)])
