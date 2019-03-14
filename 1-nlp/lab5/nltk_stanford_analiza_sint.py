###############################################################################
# Se da un fisier cu 5 fraze in engleza (le scrieti voi). Scrieti un program
# in Python care foloseste nltk si parserul de la Stanford. Acesta va genera
# un fisier de output cu parsarea propozitiilor bazata pe constituenti, si
# analiza bazata pe relatii de dependenta. Pentru fiecare propozitie va fi in
# fisier o intrare de forma:
#       Propozitia i
#       [Textul propozitiei i]
#       [Parsarea propozitiei i prin constituenti]
#       [Parsarea propozitiei i prin relatii de dependenta]
#       ---------------------------------------------
# Sub fiecare set de informatii pentru o propozitie avem si un separator.
# Identificatorul i va reprezenta numarul propozitiei. Ce apare in formatul
# de output intre paranteze drepte trebuie inlocuit cu informatia indicata
# intre paranteze.
###############################################################################

import os
import nltk
from nltk.parse.stanford import StanfordParser
from nltk.tag.stanford import StanfordPOSTagger
from nltk.parse.stanford import StanfordDependencyParser

os.environ['JAVAHOME'] = "/bin/java"
os.environ['STANFORD_PARSER'] = "/home/t3rtius/stanford-parser/" + \
    "stanford-parser-full-2018-10-17/stanford-parser.jar"
os.environ['STANFORD_MODELS'] = "/home/t3rtius/stanford-parser/" +\
    "stanford-parser-full-2018-10-17/stanford-parser-3.9.2-models.jar"
cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"
cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"
cale_parser = os.environ['STANFORD_PARSER']
cale_modele = os.environ['STANFORD_MODELS']

tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)
parser = StanfordParser(model_path="/home/t3rtius/stanford-parser/" +
                        "stanford-parser-full-2018-10-17/englishPCFG.ser.gz")
dependency_parser = StanfordDependencyParser(path_to_jar=cale_parser,
                                             path_to_models_jar=cale_modele)

propsIn = open("2-props.txt", "r")
propsOut = open("2-props-out.txt", "w")
propsInText = propsIn.read()
sents = nltk.sent_tokenize(propsInText)
parsed = parser.raw_parse_sents(sents)

count = 1
constituenti = []
dependente = []

for propL in parsed:
    for prop in propL:
        constituenti.append(str(prop))

for prop in sents:
    deps = dependency_parser.raw_parse(str(prop))
    for dep in deps:
        dependente.append(str(list(dep.triples())))

for prop in sents:
    propsOut.write("Propoziția " + str(count) + ":\n")
    propsOut.write(str(prop))
    propsOut.write("\n")
    propsOut.write("Parsare prin CONSTITUENȚI:" + "\n")
    propsOut.write(constituenti[count-1])
    propsOut.write("\n")
    propsOut.write("Parsare prin DEPENDENȚE:" + "\n")
    propsOut.write(dependente[count-1])
    propsOut.write("\n")
    count += 1
    propsOut.write("--------------------------------------------------")
    propsOut.write("\n")

propsIn.close()
propsOut.close()
