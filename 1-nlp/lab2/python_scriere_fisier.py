###############################################################################
# python_scriere_fisier.py
# Se considera un fisier cu numele input.txt cu un text continand cuvinte
# separate prin spatii si linii noi. Se afiseaza lista de comenzi de mai jos.
# Se vor astepta continuu comenzi, pana cand se da si ultima comanda,
# de iesire.
#       Comenzi:
#       1) scrie_continut
#       2) scrie_cuvinte [ord|asc|desc]
#       3) scrie_linii lin1-lin2
#       4) iesire
# Rezultatul pentru apelul fiecarei comenzi se va scrie intr-un fisier cu
# numele rezultat_i.txt unde i e numarul comenzii. Fisierul se va suprascrie
# in caz ca se repeta comanda (indiferent de parametri).
#       Prima comanda nu are parametri si doar scrie continutul fisierului
# input in fisierul rezultat.
#       A doua comanda are parametrii ord (pentru scrierea - in fisierul
# rezultat - a cuvintelor din text, fiecare pe o linie noua in ordinea in care
# apar in fisierul input.txt), asc (pentru scrierea cuvintelor din text, in
# ordine alfabetica), desc (pentru scrierea cuvintelor din text, in ordine
# inversa alfabetica).
#       A treia comanda primeste ca parametru doua numere de linii separate
# prin linioara lin1-lin2 (de exemplu 3-5) si afiseaza in fisier toate liniile
# cu indici intre cele doua numere (inclusiv cu indicii lin1 si lin2). Fiecare
# linie se va afisa pe un rvnd nou si in fisierul rezultat fiind precedata de
# indicele ei si simbolul ")".
#       Comanda iesire e pentru a iesi din progam.
# In plus, va exista si un fisier log.txt in care se vor adauga comenzile
# date (fiecare pe cate o linie). Fisierul nu se va suprascrie la rulare ci va
# contine si comenzile din rulari anterioare. Comenzile dintre doua rulari vor
# fi separae printr-o linie de caractere "#"
###############################################################################
