###############################################################################
# Rezolvati urmatoarele cerinte. Pentru fiecare cerinta afisati cate
# milisecunde a durat procesarea.
# 1. Afisati partile de vorbire pentru textul "I saw a cat running after a
# mouse"
# 2. Scrieti o functie care primeste un nume de parte de vorbire si un text
# (eventual dintre cele din book) si returneaza toate cuvintele care sunt de
# acel tip din text in ordinea aparitiei in text. Daca folositi textele din
# book sariti peste partea de titlu.
# 3. Scrieti o functie care primeste o lista cu parti de vorbire si un text
# (eventual dintre cele din book) si returneaza toate cuvintele care sunt de
# acele tipuri din text in ordinea aparitiei in text. Exemplificati functia
# afisand toate substantivele si verbele.
# 4. Calculati un dictionar in care cheile sunt parti de vorbire si valorile
# sunt numarul de cuvinte din text cu acea parte de vorbire. Afisati graficul
# pentru primele N valori (cele mai frecvente parti de vorbire).
###############################################################################

import nltk
from nltk.corpus import gutenberg
from nltk.tag.stanford import StanfordPOSTagger
from nltk import FreqDist
import timeit

cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"

cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"


tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)

start = timeit.timeit()
prop = "I saw a cat running after a mouse"
toks = nltk.word_tokenize(prop)
parts = tagger.tag(toks)
print("Părțile de vorbire din propoziție sînt:")
print(parts)
end = timeit.timeit()
durata = 10**3*abs(end-start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()


def parti(pos, txt):
    tokens = nltk.word_tokenize(txt)
    poss = dict(tagger.tag(tokens))
    partsLikePos = [part for part in poss.keys() if poss.get(part) == pos]
    return partsLikePos


textTest = "There once was a Prince who lived in a castle. " + \
    "His name was Fat-Frumos and he fought the Big Zmeu."
print("Verbele din textul:")
print(">> " + textTest)
print("sînt:")
print(parti('VBD', textTest))
end = timeit.timeit()
durata = 10**3*abs(end-start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")


start = timeit.timeit()


def partsList(lista, text):
    tokens = nltk.word_tokenize(text)
    parti = dict(tagger.tag(tokens))
    partsFromList = [part for part in parti.keys() if parti.get(part) in lista]
    return partsFromList


print("Substantivele și verbele din textul")
print(">> " + textTest)
print("sînt:")
print(partsList(['VBD', 'NN'], textTest))
end = timeit.timeit()
durata = 10**3*abs(end-start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")


start = timeit.timeit()


def graficFrecvWhitman(numar):
    textRaw = gutenberg.raw('whitman-leaves.txt')
    pos_list = nltk.pos_tag(textRaw)
    fd = FreqDist(pos_list)
    primeleN = FreqDist(dict(fd.most_common()[:numar]))
    primeleN.plot()


print("Primele 5 părți de vorbire din Walt Whitman - Leaves of Grass")
print("sînt reprezentate grafic.")
graficFrecvWhitman(5)
end = timeit.timeit()
durata = 10**3*abs(end-start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("====================PROGRAM TERMINAT====================")

###############################################################################
# Observație:
# - Probabil că există o varianta mai elegantă de a cronometra execuția,
# folosind profilers sau ceva de felul ăsta, dar nu le stăpînesc suficient
# de bine, așa că am ales varianta destul de neelegantă, cu timeit.
###############################################################################
