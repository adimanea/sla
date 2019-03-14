###############################################################################
# Rezolvati urmatoarele cerinte. Pentru fiecare cerinta afisati cate
# milisecunde a durat procesarea. Puteti refolosi functii de la exercitiile
# anterioare.
# Cautati un text scurt in limba engleza (de exemplu de pe
# wikipedia si puneti-l intr-un fisier.
# 1. Cititi textul din fisier si tokenizati-l. Afisati rezultatul intr-un
# fisier out.txt.
# 2. Afisati in fisierul out.txt cate propozitii sunt.
# 3. Afisati in fisierul out.txt pentru fiecare propozitie urmatoarele
# infomatii:
#       3a. Textul propozitiei (inclusiv semnele de punctuatie)
#       3b. Cate cuvinte are fiecare propozitie
#       3c. Cate stopwords are fiecare propozitie.
#       3d. Sa se afiseze cuvintele care nu sunt stop words.
#       3e. Analiza morfologica a propozitiei.
#       3f. Procentul de cuvinte tematice (substantive si verbe are
#           fiecare propozitie).
###############################################################################

import nltk
from nltk.tag.stanford import StanfordPOSTagger
from nltk.corpus import stopwords
import timeit

cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"

cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"


tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)


start = timeit.timeit()
tokeF = open("toke-in.txt", "r")
tokeText = tokeF.read()
toks = nltk.word_tokenize(tokeText)
tokeO = open("out.txt", "w")
tokeO.write("1. Tokenizarea textului din fișierul de intrare:\n")
tokeO.write(str(toks))
tokeO.write("\n")
end = timeit.timeit()
durata = 10**3*abs(end-start)
tokeO.write("Procesarea a durat ")
tokeO.write("% 5.2f" % durata + " milisecunde.\n")
tokeO.write("------------------------------------------------------------")
tokeO.write("\n")

start = timeit.timeit()
props = nltk.sent_tokenize(tokeText)
tokeO.write("2. Textul conține " + str(len(props)) + " propoziții.")
tokeO.write("\n")
end = timeit.timeit()
durata = 10**3*abs(end-start)
tokeO.write("Procesarea a durat ")
tokeO.write("% 5.2f" % durata + " milisecunde.\n")
tokeO.write("------------------------------------------------------------")
tokeO.write("\n")

start = timeit.timeit()
stopWords = set(stopwords.words('english'))
tokeO.write("Propozițiile textului sînt:\n")
count = 0
for prop in props:
    count += 1
    tokeO.write(str(count) + ". " + prop + "\n")
    cuvInProp = nltk.word_tokenize(prop)
    tokeO.write("Propoziția are " + str(len(cuvInProp)) +
                " cuvinte.\n")
    end = timeit.timeit()
    durata = 10**3*abs(end-start)
    tokeO.write("Procesarea a durat ")
    tokeO.write("% 5.2f" % durata + " milisecunde.\n")
    tokeO.write("------------------------------------------------------------")
    tokeO.write("\n")
    start = timeit.timeit()
    setCuvInProp = set(cuvInProp)
    stopInProp = setCuvInProp.intersection(stopWords)
    tokeO.write("Propoziția are " + str(len(stopInProp)) + " stopwords.\n")
    end = timeit.timeit()
    durata = 10**3*abs(end-start)
    tokeO.write("Procesarea a durat ")
    tokeO.write("% 5.2f" % durata + " milisecunde.\n")
    tokeO.write("------------------------------------------------------------")
    tokeO.write("\n")
    start = timeit.timeit()
    tokeO.write("Cuvintele care nu sînt stopwords sînt:\n")
    tokeO.write(str(setCuvInProp.difference(stopWords)) + "\n")
    end = timeit.timeit()
    durata = 10**3*abs(end-start)
    tokeO.write("Procesarea a durat ")
    tokeO.write("% 5.2f" % durata + " milisecunde.\n")
    tokeO.write("------------------------------------------------------------")
    tokeO.write("\n")
    start = timeit.timeit()
    morfo = tagger.tag(cuvInProp)
    tokeO.write("Analiza morfologică a propoziției este:\n")
    tokeO.write(str(morfo) + "\n")
    end = timeit.timeit()
    durata = 10**3*abs(end-start)
    tokeO.write("Procesarea a durat ")
    tokeO.write("% 5.2f" % durata + " milisecunde.\n")
    tokeO.write("------------------------------------------------------------")
    tokeO.write("\n")
    start = timeit.timeit()
    verbe = 0
    substantive = 0
    partiTotal = 0
    morfoDict = dict(morfo)
    for parte in morfoDict.values():
        if 'VB' in parte:
            verbe += 1
        if 'NN' in parte:
            substantive += 1
        partiTotal += 1
    procVerbe = verbe/partiTotal * 100
    procSubst = substantive/partiTotal * 100
    procTematice = (substantive + verbe)/partiTotal * 100
    tokeO.write("Propoziția are % 5.2f %%" % procVerbe + " verbe \n")
    tokeO.write("și % 5.2f %%" % procSubst + " substantive, deci \n")
    tokeO.write("% 5.2f %%" % procTematice + " cuvinte tematice.\n")
    end = timeit.timeit()
    durata = 10**3*abs(end-start)
    tokeO.write("Procesarea a durat ")
    tokeO.write("% 5.2f" % durata + " milisecunde.\n")
    tokeO.write("\n")

tokeO.write("====================PROGRAM TERMINAT====================")

tokeO.close()
tokeF.close()

###############################################################################
# Observație:
# - Probabil că există o varianta mai elegantă de a cronometra execuția,
# folosind profilers sau ceva de felul ăsta, dar nu le stăpînesc suficient
# de bine, așa că am ales varianta destul de neelegantă, cu timeit.
###############################################################################
