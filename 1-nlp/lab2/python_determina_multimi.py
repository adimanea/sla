###############################################################################
# python_determina_multimi.py
# a. Creati o functie cu 3 parametri
# calculeaza1(AuB,AiB,AmB)
# Functia va avea rolul de a determina multimile A si B, avand in vedere ca
# parametrii reprezinta multimile A reunit cu B, A intersectat cu B si A-B.
# Functia va returna rezultatul sub forma unui tuplu cu cele doua liste.
# b. Creati o functie cu 3 parametri
# calculeaza2(AiB,AmB,BmA)
# Functia va avea rolul de a determina multimile A si B, avand in vedere ca
# primii 3 parametri reprezinta multimile A intersectat cu B, A-B si B-A.
###############################################################################


def calculeaza1(AuB, AiB, AmB):
    print("A = ", end="")
    print(set(AmB) | set(AiB))
    print("B = ", end="")
    print(set(AuB) - set(AmB))


print("Mulțimile, obținute știind reuniunea, intersecția și diferența:")
calculeaza1({"a", "b", "c", "d"}, {"a"}, {"b"})

###############################################################################


def calculeaza2(AiB, AmB, BmA):
    print("A = ", end="")
    print(set(AiB) | set(AmB))
    print("B = ", end="")
    print(set(BmA) | set(AiB))


print("Mulțimile, obținute știind intersecția și diferențele:")
calculeaza2({1}, {2, 3}, {4, 5})
