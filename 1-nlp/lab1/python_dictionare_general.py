###############################################################################
# python_dictionare_general.py
# Se dă o listă de șiruri despărțite prin cratimă.
# 1. Creați un dicționar (enumerîndu-i elementele) cu cheile și valorile
# următoare: ("vocale", "aeiou"), ("consoane", "bcd.."), ("cifre","012..9").
# 2. Să se calculeze un dicționar pe baza listei de șiruri, unde cheile sînt
# părțile de cuvînt, iar valoarea corespunzătoare pentru fiecare cheie este
# lista cu cuvintele care conțin acea parte de cuvînt.
# 3. Din dicționarul rezultat, să se elimine cheile formate din cifre
# și să se afișeze perechile cheie-valoare eliminate.
# 4. Să se afișeze cîte chei au rămas în dicționar.
# 5. Să se calculeze și afișeze lista cu silabe de forma consoană-vocală-
# consoană.
###############################################################################

dictionar = {
    "vocale": "aeiou",
    "consoane": "bcdfghjklmnpqrstvxyz",
    "cifre": "0123456789"
}

cuvinte = ["co-pa-cel", "pa-pu-cel", "a-bac", "021-220-20-10",
           "1-pi-tic", "go-go-nea", "tip-til", "123-456",
           "a-co-lo", "lo-go-ped", "pa-pa-gal", "co-co-starc"]

cuvinteStrip = [cuvint.split("-") for cuvint in cuvinte]


def flatten(lst):
    return [item for sublist in lst for item in sublist]


silabe = list(set(flatten(cuvinteStrip)))
dictionar2 = dict.fromkeys(silabe, [])
for part in dictionar2.keys():
    dictionar2[part] = [cuvSil for cuvSil in cuvinte if part in cuvSil]
    # problemă: a in "co-pa-cel" și nu e clar dacă ar trebui
print(dictionar2)
print("Avem " + str(len(dictionar2)) + " chei")
print("--------------------")

# lucrez cu o copie, deoarece dicționarul își schimbă mărimea
# și am eroare la iterație după chei.
dcopy = dictionar2.copy()
for cheie in dcopy.keys():
    if any(i.isdigit() for i in cheie):
        print("Elimin " + str(cheie) + ": " + str(dcopy[cheie]))
        del dictionar2[cheie]
print("Au mai rămas " + str(len(dictionar2)) + " chei")
print("--------------------")

print("Silabe cu CVC: ")
for cons in dictionar["consoane"]:
    for voc in dictionar["vocale"]:
        for con in dictionar["consoane"]:
            cvc = cons + voc + con
            for silaba in silabe:
                if cvc in silaba:
                    print(silaba)
# Nu e clar dacă "starc" ar trebui să intre sau ar trebui să fie
# DOAR CVC, fără alte litere.
