###############################################################################
# Se dă o listă de cuvinte.
# Sa se scrie o functie gen_matrice(). Functia genereaza (indiferent de
# susbsetul de litere folosite in cuvinte) matricea avand liniile si coloanele
# corespunzatoare tuturor literelor din alfabet (pentru simplitate folosim
# alfabetul englezesc - deci fara caractere Unicode speciale precum litere
# cu diacritice). Prima linie si prima coloana vor contine chiar litere
# alfabetului in ordine, restul matricii va fi completat cu 0.
# 2. Sa se scrie o alta functie, completeaza_matrice(), care primeste ca
# parametru lista de cuvinte si matricea creata mai devreme. Functia va
# modifica matricea astfel incat un element de pe pozitia i+1,j+1 reprezinta
# numarul de dati in care litera corespunzatoare liniei i s-a aflat intr-un
# cuvant in urma literei corespunzatoare coloanei j. Se va apela functia si
# se va afisa matricea.
# 3. Sa se elimine din matrice liniile si coloanele cu toate elementele 0.
# Sa se afiseze matricea.
# 4. Sa se afiseze perechile (distincte) de litere cu numarul de aparitii
# mai mare sau egal decat un N (dati voi o valoare, de exemplu 2).
###############################################################################

import string

litere = list(string.ascii_lowercase)
cuvinte = ["papagal", "pisica", "soarece", "bolovan",
           "soparla", "catel", "pasare"]


def gen_matrice():
    rows, cols = len(litere), len(litere)
    matrice = [[0 for c in range(cols)] for r in range(rows)]
    matrice[0] = [litera for litera in litere]
    for j in range(26):
        matrice[j][0] = litere[j]
    return matrice


m = gen_matrice()


def completeaza_matrice(matx, listaCuv):
    matx = gen_matrice()
    for i in range(1, 26):
        for j in range(1, 26):
            pereche = str(matx[0][j-1]) + str(matx[i-1][0])
            for cuvint in listaCuv:
                matx[i][j] += cuvint.count(pereche)
    return matx


mt = completeaza_matrice(m, cuvinte)
print(mt)

# hacky, folosesc copie, nu șterg efectiv...
mcopy = mt
for i in range(1, 26):
    semafor = 0
    for j in range(1, 26):
        if (mt[i][j] != 0):
            semafor = 1
    if semafor:
        mcopy[i] = mt[i]
    else:
        mcopy[i] = ["@"]

# acum șterg
mcopy = [elem for elem in mcopy if len(elem) > 1]
print(mcopy)

linii = 0
for i in mcopy:
    linii += 1
for i in range(1, linii):
    for j in range(1, 26):
        if mcopy[i][j] >= 4:
            print(str(mcopy[0][j-1]) + str(mcopy[i-1][0]))
