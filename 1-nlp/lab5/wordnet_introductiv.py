###############################################################################
# Rezolvati urmatoarele cerinte. Toate functiile definite trebuie si apelate
# pentru a demonstra buna functionare.
#   1. Scrieti o functie care primeste un cuvant si afiseaza glosele asociate
# tuturor sensurilor acelui cuvant.
#   2. Scrieti o functie care primeste doua cuvinte ca parametri. Functia va
# verifica, cu ajutorul wordnet, daca cele doua cuvinte pot fi sinonime
# (exista un sens, deci un synset din care ambele sa faca parte). Afisati
# definitia pentru acel synset.
#   3. Scrieti o functie care primeste un synset si returneaza un tuplu cu
# doua liste. Prima lista este lista holonimelor (indiferent de tipul lor) si
# a doua lista este cea a meronimelor (indiferent de tipul lor). Gasiti un
# cuvant care are holonime si/sau meronime de diferite tipuri. Afisati-le
# intai separat si apoi pe toate folosind functia creata.
#   4. Scrieti o functie care afiseaza pentru un synset drumul de hipernime,
# mergand de la hipernimul imediat la hipernimul lui si apoi la hipernimul
# hipernimului si tot asa pana la cel mai de sus hipernim.
#   5. Sa se scrie o functie care primeste ca parametri doua synset-uri.
# Consideram d1(k) numarul de deplasari din hipernim in hipernim de la
# cuvantul 1 pana la un hipernim k si d2(k) numarul de deplasari din
# hipernim in hipernim de la cuvantul 2 pana la un hipernim k . Functia va
# returna lista hipernimelor cu proprietatea ca d1(k)+d2(k) este minim (unde
# k ar fi fiecare hipernim in parte; evident pentru toate hipernimele, suma
# este aceeasi).
#   6. Consideram o functie care primeste un synset si o lista de synseturi
# (cu minim 5 elemente in lista cand testati). Functia va returna lista
# sortata dupa similaritatea intre primul cuvant si cuvintele din lista.
# De exemplu (consideram ca luam primul synset pentru fiecare cuvant) putem
# testa pentru cuvantul cat si lista de cuvinte: animal, tree, house, object,
# public_school, mouse.
#   7. Scrieti o functie care verifica pentru doua synseturi daca pot fi
# meronime indirecte pentru acelasi synset. Prin meronim indirect intelegem
# un element care poate face parte din holonim sau dintr-un element care este
# parte direct sau indirect din holonim. (atentie este vorba de orice tip
# de meronime dintre cele 3).
#   8. Sa se afiseze sinonimele si antonimele unui adjectiv (de exemplu
# "beautiful"). In cazul in care are mai multe sensuri se vor afisa separat
# pentru fiecare sens, afisand inainte de asta si definitia pentru acel sens.
###############################################################################

from nltk.corpus import wordnet as wn


def glose(cuv):
    synL = wn.synsets(cuv)
    count = 1
    print("Glose pentru cuvîntul " + cuv.upper() + ":")
    for syn in synL:
        print("Glosa " + str(count) + ": " + syn.definition())
        count += 1


glose('dog')
print("------------------------------------------------------------")


def sino(cuv1, cuv2):
    synL1 = wn.synsets(cuv1)
    synL2 = wn.synsets(cuv2)
    comun = [syn for syn in synL1 if syn in synL2]
    if not comun:
        print("Cuvintele " + cuv1.upper() + " și " + cuv2.upper() +
              " nu au niciun synset comun.")
    elif len(comun) == 1:
        print("Definiția comună pentru " + cuv1.upper() + " și " +
              cuv2.upper() + " este:")
        print(" > " + comun[0].definition())
    else:
        print("Definițiile comune pentru " + cuv1.upper() + " și " +
              cuv2.upper() + " sînt:")
        for synCom in comun:
            print(" > " + synCom.definition())


sino('house', 'home')
sino('dog', 'mouse')
print("----------------------------------------------------------------------")


def holomero(ss):
    holo = []
    mero = []
    holo.append(ss.substance_holonyms())
    holo.append(ss.part_holonyms())
    holo.append(ss.member_holonyms())
    mero.append(ss.substance_meronyms())
    mero.append(ss.part_meronyms())
    mero.append(ss.member_meronyms())
    hm = zip(holo, mero)
    print("Holonime tip substanță: " + str(ss.substance_holonyms()))
    print("Meronime tip substanță: " + str(ss.substance_meronyms()))
    print("Holonime tip parte: " + str(ss.part_holonyms()))
    print("Meronime tip parte: " + str(ss.part_meronyms()))
    print("Holonime tip membru: " + str(ss.member_holonyms()))
    print("Meronime tip membru: " + str(ss.member_meronyms()))
    print("Tuplul cu holonime și meronime (S, P, M) este: ")
    print(list(hm))
    print("-----------------------------------------------------------------")


holomero(wn.synsets('human')[0])


def hipPath(ss):
    hyps = []
    while ss.hypernyms():
        hyps.append(ss.hypernyms()[0])
        ss = ss.hypernyms()[0]
    print("Ierarhia de hipernime:")
    for hyp in hyps:
        print(str(hyp) + " ---> ", end="")
    print("\n--------------------------------------------------------------")


hipPath(wn.synsets('eye')[0])

######################################################################
# Nu înțeleg cerința la 5...
######################################################################


def simil(ss, listaSS):
    sims = []
    for syn in listaSS:
        sims.append(ss.path_similarity(syn))
    print(sorted(sims))
    print("------------------------------------------------------------")


pisica = wn.synset('cat.n.01')
labuta = wn.synset('paw.n.01')
ochi = wn.synset('eye.n.01')
zid = wn.synset('wall.n.01')
blana = wn.synset('fur.n.01')
alb = wn.synset('white.n.01')
seturi = [labuta, ochi, zid, blana, alb]
simil(pisica, seturi)

######################################################################
# Încercare la subpunctul 7. Dar am renunțat, pentru că nu prea
# înțeleg cerința.
######################################################################


# def flattenA(ls):
#     flat = []
#     for x in ls:
#         for y in x:
#             flat.append(y)
#     return flat


# def merIndirect(ss1, ss2):
#     holo1 = ss1.part_holonyms()
#     holo2 = ss2.part_holonyms()
#     for mbmer in ss1.member_holonyms():
#         holo1.append(mbmer)
#     for smer in ss1.substance_holonyms():
#         holo1.append(smer)
#     for mmer in ss2.member_holonyms():
#         holo2.append(mmer)
#     for smer in ss2.substance_holonyms():
#         holo2.append(smer)
#     sem = 1
#     while sem:
#         for hol1 in holo1:
#             if (not hol1.member_holonyms() and not hol1.substance_meronyms()
#                 and not hol1.part_holonyms()):
#                 sem = 0
#             else:
#                 for pmer in hol1.part_meronyms():
#                     holo1.append(pmer)
#                 for mbmer in hol1.member_meronyms():
#                     holo1.append(mbmer)
#                 for smer in hol1.substance_meronyms():
#                     holo1.append(smer)
#     print("-----------------------------------------------------------------")


# merIndirect(wn.synset('cat.n.01'), wn.synset('eye.n.01'))

######################################################################


def sinAnt(adj):
    synL = wn.synsets(adj)
    print("Cuvîntul introdus este: " + adj.upper())
    for syn in synL:
        print("Glosa: " + str(syn.definition()))
        print("Sinonim: " + str((syn.lemmas()[0].name())))
        if (syn.lemmas()[0].antonyms()):
            print("Antonim: " + str(syn.lemmas()[0].antonyms()[0].name()))
        else:
            print("Nu există antonime pentru acest sens.")
        print("------------------------------------------------------------")


sinAnt('tasty')
sinAnt('nice')
