###############################################################################
# python_citire_fisier.py
# Intr-un hol de asteptare se considera un sir de scaune numerotate cu numere
# consecutive de la 0 la numarul de scaune(necunoscut) Vom considera un
# fisier de forma:
#       2:ionel
#       7:alex
#       1:maria
#       10:ioana
#       5:liliana
#       14:george
# Se va crea o lista in care un element poate fi sirul "gol" sau numele celui
# care sta pe scaun. Pe masura ce se citesc noi randuri din fisier se adauga
# elemente in lista, sau se modifica persoana care statea pe scaun, astfel:
#       - primul rand din fisier e de forma nr:nume, atunci se adauga nr-1
# elemente de tip "gol" in lista, iar pe al nr-lea element se va pune numele
# citit din fisier
#       - repetitiv se citesc linii de forma nr:nume. Daca nr e mai mic decat
# numarul de elemente deja existente in lista, atunci se modifica al nr-lea
# element cu noul nume. Daca nr e mai mare decat ultimul indice al listei se
# completeaza cu elemente de tip "gol" pana ajunge lista la nr-1 elemente si
# apoi se adauga si numele in lista.
###############################################################################
