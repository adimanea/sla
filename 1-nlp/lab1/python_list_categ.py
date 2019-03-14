############################################################
# Se dă o listă de cuvinte. Să se afișeze cuvintele,
# împreună cu numărul aparițiilor lor (case insensitive).
############################################################

lista = ["haha", "poc", "Poc", "POC", "haHA", "hei", "hey",
         "HahA", "poc", "Hei"]

aparitii = {}
listaLower = [None]*len(lista)

for i in range(0, len(lista)):
    listaLower[i] = lista[i].lower()

for cuvint in listaLower:
    if cuvint not in aparitii:
        aparitii[cuvint] = 0
    aparitii[cuvint] += 1

for (k, v) in aparitii.items():
    print("aparitii[{}] = {}".format(k, v))
