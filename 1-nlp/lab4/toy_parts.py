import nltk
from nltk.tag.stanford import StanfordPOSTagger

cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"

cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"


tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)

text = "There once was a prince and he lived in a castle " +\
    "and his name was Prince Charming."

cuvInProp = nltk.word_tokenize(text)
morfo = tagger.tag(cuvInProp)
print("Analiza morfologică este:")
morfoDict = dict(morfo)
for parte in morfoDict.values():
    print(parte)
