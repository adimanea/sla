###############################################################################
# python_citire_scriere_fisier.py
# Sa se scrie o functie care primeste ca parametru un nume de fisier. Functia
# va deschide fisierul in modul "r+", citind si schimband continutul fisierului
# in acelasi timp. Functia va elimina liniile goale si spatiile multiple din
# fisier, returnand cate caractere a sters. Sa se apeleze functia pe un fisier
# dat (se va uploada si fisierul in formatul initial si fisierul rezultat).
###############################################################################
# regex pentru căutare mai ușoară de spații multiple
import re


def elimina(fisier):
    myFile = open(fisier, "r+")
    linii = myFile.readlines()
    myFile.write("\n---------------------OUT--------------------------\n")
    liniiNeGoale = []
    for linie in linii:
        if not len(linie.strip()) == 0:
            liniiNeGoale.append(linie)
    spatii = [0]*80
    index = -1
    for linieNeGoala in liniiNeGoale:
        index += 1
        goaleCount = linieNeGoala.count(" ")
        spatii[index] = goaleCount
        linieNeGoala = re.sub(" +", " ", linieNeGoala)
        myFile.write(linieNeGoala)
    charEliminate = 0
    for spatiu in spatii:
        if spatiu != 0:
            charEliminate += spatiu - 1
    myFile.write("S-au eliminat " + str(charEliminate) + " caractere")
    myFile.close()


elimina("citire_scriere.txt")
