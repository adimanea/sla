###############################################################################
# Rezolvati urmatoarele cerinte. Pentru fiecare cerinta afisati cate
# milisecunde a durat procesarea. In subpunctele de mai jos prin cuvinte
# intelegem siruri formate din litere sau cifre.
# 1. Instalati nltk in cazul in care nu e deja instalat. Downloadati
# resursele necesare pentru acest exercitiu (book). Veti folosi textul 2.
# 2. Afisati cate cuvinte are textul.
# 3. Afisati titlul textului.
# 4. Afisati lungimea vocabularului textului. Consideram ca in vocabular nu
# intra si numerele sau sirurile corespunzatoare semnelor de punctuatie.
# 5. Scrieti o functie care returneaza numarul de cuvinte de lungime L.
# Apelati functia.
# 6. Scrieti o functie care afiseaza primele N cuvinte distincte (din
# vocabularul ordonat alfabetic) care incep cu litera L. Apelati functia.
# 7. Afisati cel mai lung si cel mai scurt cuvant din text. In cazul in care
# sunt mai multe cuvinte de lungime minima sau maxima, se afiseaza toate.
# 8. Afisati primele N cele mai frecvente cuvinte (formate din litere sau
# cifre)  din text impreuna cu numarul de aparitii.
# 9. Afisati lungimea medie a cuvintelor din text
# 10. Afisati cuvintele care apar o singura data in text.
# 11. Afisati colocatiile din text.
###############################################################################

import string
import nltk
from nltk.book import text2
from nltk.tag.stanford import StanfordPOSTagger
import timeit
from nltk.probability import FreqDist
import nltk.collocations

cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"

cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"


tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)

start = timeit.timeit()
cuvinteT2 = len(text2)
print("Textul 2 are " + str(cuvinteT2) + " cuvinte.")
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()
print("Titlul este: " + text2.name)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")


start = timeit.timeit()
punct = list(string.punctuation)
num = list(string.digits)
tok2 = list(set(text2.tokens))
vocabT2 = [word for word in tok2 if word.isalpha()]
print("Vocabularul textului are " + str(len(vocabT2)) + " cuvinte")
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()


def cuv(lung):
    cuvinte = []
    for cuvint in vocabT2:
        if len(cuvint) == lung:
            cuvinte.append(cuvint)
    return cuvinte


print("Cuvintele cu 17 litere sînt: ")
print(cuv(17))
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()


def cuvNL(nr):
    cuvinte = []
    vocabSorted = sorted(vocabT2)
    for cuvint in vocabSorted:
            if cuvint[0] == 'L' and len(cuvinte) < nr:
                cuvinte.append(cuvint)
    print(cuvinte)


print("Primele 10 cuvinte care încep cu L sînt:")
cuvNL(10)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()
vocabSortat = sorted(vocabT2, key=len)
primul = vocabSortat[0]
ultimul = vocabSortat[-1]
minime = []
maxime = []
for cuvint in vocabSortat:
    if len(cuvint) == len(primul):
        minime.append(cuvint)
    if len(cuvint) == len(ultimul):
        maxime.append(cuvint)
print("Cuvintele de lungime maximă sînt:")
print(maxime)
print("Cuvintele de lungime minimă sînt:")
print(minime)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()


def frec(n):
    fdist2 = FreqDist(text2)
    print(fdist2.most_common(n))


print("Primele 5 cele mai frecvente token-uri sînt:")
frec(5)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()
medie = sum(len(cuv) for cuv in vocabT2)/len(vocabT2)
print("Lungimea medie a cuvintelor este:")
print(medie)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()
fdist = FreqDist(text2)
apare1 = [cv for cv in fdist.keys() if fdist.get(cv) == 1]
print("Cuvintele care apar doar o dată:")
print(apare1)
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("------------------------------------------------------------")

start = timeit.timeit()

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(text2)
print("Primele 10 colocații (pentru bigrame) sînt:")
print(finder.nbest(bigram_measures.pmi, 10))
end = timeit.timeit()
durata = 1000*abs(end - start)
print("Procesarea a durat ", end=" ")
print("% 5.2f" % durata + " milisecunde ")
print("==========================PROGRAM TERMINAT==========================")

###############################################################################
# Observație:
# - Probabil că există o varianta mai elegantă de a cronometra execuția,
# folosind profilers sau ceva de felul ăsta, dar nu le stăpînesc suficient
# de bine, așa că am ales varianta destul de neelegantă, cu timeit.
###############################################################################
