############################################################
# Se alege aleator un număr întreg între un Nmic și un Nmare.
# Utilizatorul are X încercări de a ghici numărul. La fiecare
# încercare, i se spune dacă numărul e mai mare sau mai mic
# decît ce a introdus. Implementați iterativ.
############################################################

import random


Nmic, Nmare, X = 0, 20, 5
numar = random.randint(Nmic, Nmare)
print("Ghicește un număr de la " + str(Nmic) + " la " + str(Nmare))
print("din " + str(X) + " încercări.")
ghici = int(input())
for i in range(0, int(X) - 1, 1):
    if ghici < numar:
        print("Mai mult!")
        ghici = int(input())
    if ghici > numar:
        print("Mai puțin!")
        ghici = int(input())
    if ghici == numar:
        print("FIX!")
        break
print("====GAME OVER====")
