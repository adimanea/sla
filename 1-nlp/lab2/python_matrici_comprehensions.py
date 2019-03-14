###############################################################################
# python_matrici_comprehensions.py
# Rezolvati subpunctele urmatoare folosind list comprehensions.
#       1. Sa se scrie o functie care genereaza o matrice de dimensiune n*n,
# unde n este un argument dat functiei.Prima linie va avea forma [1,1,1,1..,1]
# de n ori, a doua linie va avea forma [2,2,2....,2] de n-ori, pana la a n-a
# linie care va avea forma [n,n,n,...,n] de n ori. De exemplu, pentru n=4:
#    [[1,1,1,1],
#    [2,2,2,2],
#    [3,3,3,3],
#    [4,4,4,4]]
#    Sa se apeleze functia si sa se afiseze rezultatul.
#       2. Sa se scrie o functie care primeste ca parametru o matrice m
# si returneaza matricea rezultata prin copierea doar a coloanelor cu indici
# impari din m.
#    Sa se apeleze functia si sa se afiseze rezultatul.
#       3. Sa se scrie o functie numita sita care va primi ca parametri doua
# matrici de dimensiuni egale. Prima matrice va contine elemente diverse.
# A doua va contine doar elemente 0 si 1. A doua matrice va functiona ca o
# sita pentru prima. Functia va returna o matrice care va contine 0 in locurile
# unde a doua matrice avea valoarea 0 si elementul corespunzator din prima
# matrice in locurile unde a doua matrice avea valoarea 1. De exemplu,
# pentru matricile:
# 2 5 7 1
# 4 5 0 2
# 0 3 1 7

# 1 0 0 1
# 0 1 1 0
# 0 1 0 1
# matricea rezultata va fi:
# 2 0 0 1
# 0 5 0 0
# 0 3 0 7
#    Sa se apeleze functia si sa se afiseze rezultatul.
#       4. Sa se scrie o functie care primeste ca parametri doua numere n si
# elem si calculeaza o matrice de dimensiune n*n in care toate elementele
# sunt 0, cu exceptia diagonalei a doua unde toate sunt egale cu elem.
# De exemplu, pentru n=3, matricea ar fi: [[0,0,1], [0,1,0], [1,0,0]]
#       5.Sa se scrie o functie care primeste doua liste de numere, l1 si l2
# si returneaza o matrice cu numarul de linii egal cu numarul de elemente din
# l1 si numarul de coloane egal cu numarul de elemente din l2. Matricea pe
# fiecare element de pe linia i, coloana j, va avea doar valori de forma:
#        l1[i] (daca elementul de pe pozitia i din l1 e mai mic sau egal
# decat elementul de pe pozitia j din l2)
#        l2[i] (daca elementul de pe pozitia i din l1 e mai mare decat
# elementul de pe pozitia j din l2)
###############################################################################

import random


def matriceGen(dim):
    print([[x] * dim for x in range(1, dim + 1)])


print("1. Generare matrice: ")
matriceGen(5)


def coloanePare(mat):
    print([[linie[i] for i in range(len(mat[0])) if i % 2 == 0]
           for linie in mat])


print("2. Matricea cu elementele de pe coloanele pare: ")
coloanePare([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])


def sita(nr):
    mat1 = [[random.randint(1, 10) for i in range(1, nr + 1)]
            for j in range(1, nr + 1)]
    mat2 = [[random.randint(0, 10) % 2 for i in range(1, nr + 1)]
            for j in range(1, nr + 1)]
    matCernut = [[linie1[i] * linie2[i] for i in range(nr)]
                 for linie2, linie1 in zip(mat2, mat1)]
    print("Matricea: " + str(mat1))
    print("Sita: " + str(mat2))
    print("Matricea prin sită: " + str(matCernut))


print("3. Matrice aleatorie printr-o sită aleatorie:")
sita(3)


def diag2(nr, elem):
    mat = [[elem if i == nr - j - 1 else 0 for i in range(nr)]
           for j in range(nr)]
    print(mat)


print("4. Matrice cu a doua diagonală prestabilită, în rest 0:")
diag2(5, 1)


def matL1L2(l1, l2):
    mat = [[l2[j] if l1[i] > l2[j] else l1[i] for j in range(len(l2))]
           for i in range(len(l1))]
    print(mat)


print("5. Matrice din două liste:")
matL1L2([1, 2, 3, 4], [5, 0, 1])
