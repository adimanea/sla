###############################################################################
# python_multimi_comprehensions.py
# Rezolvati subpunctele urmatoare folosind set comprehensions.
#       1. Sa se scrie o functie care primeste ca parametru o lista de siruri
# si genereaza multimea totala a literelor din care sunt formate sirurile.
# Gasiti o solutie care nu foloseste reuniune. Pentru lista ["abcd","bau",
# "daca", "buf"] multimea litereleor e {"a","b","c","d","f","u"}
#       Sa se apeleze functia si sa se afiseze rezultatul.
#       2. Sa se scrie o functie care primeste ca parametru o matrice si
# calculeaza multimea elementelor de pe coloanele pare.
#       Sa se apeleze functia si sa se afiseze rezultatul.
###############################################################################


def multimeLitere(listaSiruri):
    print(set(car for sir in listaSiruri for car in sir))


print("Mulțimea literelor: ")
multimeLitere(["abcd", "bau", "daca", "buf"])  # {'b', 'f', 'c', 'u', 'a', 'd'}


###############################################################################


def sumaColPare(matrice):
    cols = len(matrice[0])
    elts = [linie[i] for linie in matrice for i in range(cols) if i % 2 == 0]
    print(sum(elts))


print("Suma elementelor de pe coloane pare: ")
sumaColPare([[0, 1, 2], [3, 4, 5]])     # 10 = (0 + 2) + (3 + 5)
# nu-mi dau seama cum ar trebui cu mulțimi, mai ales că ar elimina repetițiile
# dacă, de exemplu, am elemente egale în matrice...
