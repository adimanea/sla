######################################################################
# O matrice 4x4 de intregi și se afișează meniul:
# 1. prima diagonala
# 2. a doua diagonala
# 3 conturul
# 4. suma elementelor
# 5. iesire
# Dacă nu se dă o opțiune corectă, se repetă întrebarea.
######################################################################

matrice = [[11, 12, 13, 14], [21, 22, 23, 24],
           [31, 32, 33, 34], [41, 42, 43, 44]]

print("""
Meniu:
1. prima diagonală
2. a doua diagonală
3. conturul
4. suma elementelor
5. iesire
""")


def diag1(mat):
    for i in range(0, 4):
        print(str(mat[i][i]) + " ")


def diag2(mat):
    for i in range(0, 4):
        print(str(mat[3-i][i]) + " ")


def sumaEl(mat):
    suma = 0
    for i in range(0, 4):
        for j in range(0, 4):
            suma += mat[i][j]
    print(suma)


def contur(matrice):
    """ Dacă sîntem pe prima sau pe ultima
    linie, afișăm tot. Altfel, doar primul
    și ultimul element """
    for i in range(0, 4):
        print(str(matrice[0][i]) + " ")
    for j in range(1, 3):
        for i in range(0, 4):
            if (i == 0) or (i == 3):
                print(str(matrice[j][i]) + " ")
    for i in range(0, 4):
        print(str(matrice[3][i]) + " ")


def nimic(matrice):
    print("====PROGRAM TERMINAT====")


optiuniDict = {
    '1': diag1,
    '2': diag2,
    '3': contur,
    '4': sumaEl,
    '5': nimic
}

print("Introduceți o opțiune între 1 și 5.")


def validare():
    while True:
        optiune = input("Optiune: ")
        if optiune in optiuniDict.keys():
            optiuniDict[optiune](matrice)
            break
        else:
            print("Opțiune nevalidă. Reîncercați.")


validare()
