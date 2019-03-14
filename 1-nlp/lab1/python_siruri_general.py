######################################################################
# python_siruri_general.py
# Se dă un șir de caractere cuprinzînd un paragraf.
# 1. Să se afișeze cîte caractere are șirul.
# 2. Scrieți o funcție care primește ca parametru un șir și calculează
# lista cu toate caracterele nealfanumerice care apar în șir, cu
# excepția cratimei.
# 3. Cu ajutorul listei de caractere nealfanumerice,
# să se obțină lista cu cuvintele din paragraf (lowercase).
# Șirurile nu trebuie să conțină și spațiile din jurul cuvintelor.
# 4. Să se identifice potențialele cuvinte (substantive/numerale)
# nearticulate de gen masculin (care se termină în "ul").
# 5. Să se obțină lista șirurilor cu cratimă.
######################################################################

shir = input("Introduceți șirul: ")
print("Șirul are " + str(len(shir)) + " caractere.")


def nealfa(sir):
    lista = []
    for i in sir:
        if not(str(i).isalnum()) and (str(i) != " ") and (str(i) != "-"):
            lista.append(str(i))
    # elimină dublurile, returnează caracterul doar o dată
    return set(lista)


print("##################################################")
print("Caractere non-alfanumerice: ")
for i in nealfa(shir):
    print(str(i) + " ", end="")
print("\n##################################################")


cuvinte = []
listaCuv = shir.split()
for i in range(0, len(listaCuv)):
    for j in nealfa(shir):
        if not(j in listaCuv[i]):
            cuvinte.append(listaCuv[i])
            break
print("Cuvinte: ")
for i in cuvinte:
    print(i)
print("##################################################")


masculine = []
for i in range(0, len(cuvinte)):
    if cuvinte[i].endswith("ul"):
        masculine.append(cuvinte[i])


print("Masculine:")
for m in masculine:
    print(m)
print("##################################################")


cuCratima = []
for i in range(0, len(cuvinte)):
    if "-" in str(cuvinte[i]):
        cuCratima.append(cuvinte[i])
print("Cu cratima:")
for crat in cuCratima:
    print(crat)
