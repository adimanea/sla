###############################################################################
# File: mcb.py.
# Description: (Rudimentary) MathChatBot.
# Author: Adrian Manea.
# Disclaimer: There are a lot of elementary hacks here, I know.
#             But I had fun making it and that's what I care about.
###############################################################################
import replies as r              # predefined replies
import time                      # for keeping progress
import sys                       # for writing the log in a variable file
import os                        # no transcript wanted, write it and trash it
import random
import nltk
from nltk.corpus import wordnet as wn
from nltk.tag.stanford import StanfordPOSTagger


# Setup POS Tagger
cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"
cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"
tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)

# log file
if len(sys.argv) != 2:
    if len(sys.argv) > 2:           # too many arguments
        print("The program must be run with one mandatory argument " +
              "(program name)")
        print("and one optional argument (filename for transcript).")
        print("Please rerun it. Exiting...")
        sys.exit()
    if len(sys.argv) == 1:          # no arguments
        print("You have not chosen a transcript file.")
        print("The interaction will be showed in the console only.")
        print("You can:")
        print("(1) Continue with no transcript;")
        print("(2) Add a transcript filename;")
        print("(3) Exit.")
        co = str(input())
        while ('1' not in co and '2' not in co and '3' not in co):
            print("Invalid choice. Please retry.")
            print("You can:")
            print("(1) Continue with no transcript;")
            print("(2) Add a transcript filename;")
            print("(3) Exit.")
            co = str(input())
        if '3' in co:
            print("Exiting...")
            sys.exit()
        if '2' in co:
            print("Please input a filename with extension " +
                  "(no spaces or special characters):")
            sys.argv.append(str(input()))
        if '1' in co:
            sys.argv.append("temp.txt")
mcb = open(str(sys.argv[1]), "w")

# write execution time
mcb.write("=== " + str(sys.argv[0]) + " ===\n")
mcb.write("=== " + str(time.strftime("%c")) + " ===\n")

# Math words
gr = 'group'
lim = 'limit'
su = 'sum'
pr = 'product'
intg = 'integral'
der = 'derivative'
dif = 'differential'
exp = 'exponential'
log = 'logarithm'
fr = 'fraction'
calc = 'calculus'
an = 'analysis'
mwords = [gr, lim, su, pr, intg, der, dif, exp, log, fr, calc, an]

# Predefined verbs
study = 'study'
learn = 'learn'
practice = 'practice'
read = 'read'
exercise = 'exercise'
define = 'define'
mverbs = [study, learn, practice, read, exercise, define]

# MANUALLY add the appropriate senses...
wndb = [
    wn.synsets(gr)[0],          # group (number of entities)
    wn.synsets(gr)[2],          # group (algebra)
    wn.synsets(lim)[3],         # limit 1 (calculus)
    wn.synsets(lim)[4],         # limit 2 (boundary)
    wn.synsets(su)[1],          # sum (addition)
    wn.synsets(su)[2],          # sum ('the final aggregate')
    wn.synsets(su)[5],          # sum (set theory)
    wn.synsets(pr)[2],          # product (multiplication)
    wn.synsets(pr)[5],          # product (set theory)
    wn.synsets(intg)[0],        # integral
    wn.synsets(der)[0],         # derived_function
    wn.synsets(exp)[0],         # exponential
    wn.synsets(log)[0],         # logarithm
    wn.synsets(fr)[2],          # fraction
    wn.synsets(calc)[2],        # calculus
    wn.synsets(an)[4]           # analysis
]

polyw = [wndb[j] for j in range(0, 7)]
wndbNames = [s.lemmas()[0].name() for s in wndb]


# Conversation
greeting = random.choice(r.he)
subj = random.choice(r.topics)
print(greeting)
print(subj)
mcb.write(str(greeting) + "\n")
mcb.write(str(subj) + "\n")
for topic in mwords:
    print(topic)
    mcb.write(topic + "\n")
print("I can help you", end=" { ")
mcb.write("I can help you { ")
for vcount in range(0, len(mverbs) - 1):
    print(mverbs[vcount], end=", ")
    mcb.write(mverbs[vcount] + ", ")
print(mverbs[-1], end=" } ")
mcb.write(mverbs[-1] + " } ")
print("some of these.")
mcb.write("some of these.\n")
gb = random.choice(r.leave)
print(gb)
mcb.write(str(gb) + "\n")
reply = str(input("--> "))
mcb.write("--> " + reply + "\n")

while ('BYE' not in reply.upper()):
    # Parse the reply, looking for nouns and verbs
    tokens = nltk.word_tokenize(reply)
    parts = dict(tagger.tag(tokens))
    verbs = [part for part in parts.keys() if "VB" in parts.get(part)
             or "VP" in parts.get(part)]
    verbsUpper = [v.upper() for v in verbs]
    nouns = [part for part in parts.keys() if "NN" in parts.get(part)
             or "NP" in parts.get(part)]
    nounsUpper = [n.upper() for n in nouns]
    while (not verbs and not nouns):
        nun = random.choice(r.notu)
        bye = random.choice(r.leave)
        print(nun)
        print(bye)
        reply = str(input("--> "))
        mcb.write(str(nun) + "\n")
        mcb.write(str(bye) + "\n")
        mcb.write("--> " + reply + "\n")
    # Make list of all senses of the NOUNS in the reply
    nounSenses = [nn for noun in nouns for nn in wn.synsets(noun)]
    # Get the one which is most similar to what's in the DB
    # Make it a dictionary! {synset:similarity}
    nounSimsDict = {word.path_similarity(part): word for part in
                    nounSenses for word in wndb}
    # Store (nonzero) similarity scores separately, to get max
    nounSimsLs = [k for k in nounSimsDict.keys() if k]
    ans = False
    if nounSimsLs:
        theNounSS = nounSimsDict[max(nounSimsLs)]
        theNounSSLemma = nounSimsDict[max(nounSimsLs)].lemmas()[0]
        theNounName = theNounSSLemma.name()
        theNounDef = nounSimsDict[max(nounSimsLs)].definition()
        if ('LEARN' in verbsUpper or 'STUDY' in verbsUpper):
            print('So, you want to learn about ' + theNounName +
                  ' or something related.')
            mcb.write('So, you want to learn about ' + theNounName +
                      ' or something related.' + "\n")
            studyR = random.choice(r.studyReplies)
            print(studyR)
            mcb.write(str(studyR) + "\n")
            ans = True
        if ('EXERCISE' in verbsUpper or 'PRACTICE' in verbsUpper
           or 'EXERCISE' in nounsUpper or 'PRACTICE' in nounsUpper):
            practiceRs = random.choice(r.practiceLs)
            practiceR = random.choice(r.practiceReplies)
            mcb.write(str(practiceRs) + "\n")
            mcb.write(str(practiceR) + "\n")
            print(practiceRs)
            print(practiceR)
            ans = True
            if 'READ' in verbsUpper:
                print('There are great resources for reading about ' +
                      theNounName + ' and related stuff.')
                mcb.write('There are great resources for reading about ' +
                          theNounName + ' and related stuff.\n')
            studyR = random.choice(r.studyReplies)
            print(studyR)
            mcb.write(str(studyR) + "\n")
            ans = True
        if ('DEFINE' in verbsUpper or 'DEFINITION' in nounsUpper):
            print('I can give you the definition of ' + theNounName + '.')
            mcb.write('I can give you the definition of ' +
                      theNounName + '.\n')
            if theNounSS not in polyw:
                print("Here it is: ")
                mcb.write("Here it is: \n")
                print('> Definition: ' + theNounDef)
                mcb.write('> Definition: ' + theNounDef + "\n")
            else:
                # If polysemantic,
                # find which one of them it is
                senses = []
                for poly in polyw:
                    if poly.lemmas()[0].name() == theNounSS.lemmas()[0].name():
                        senses.append(poly)
                print("I know " + str(len(senses)) + " definitions of " +
                      theNounName + ".")
                mcb.write("I know " + str(len(senses)) + " definitions of " +
                          theNounName + ".\n")
                count = 0
                mcb.write('Here is one of them:\n')
                print('Here is one of them: ')
                print('> Definition: ' + senses[count].definition())
                mcb.write('> Definition: ' + senses[count].definition() + "\n")
                count += 1
                print("Is this what you were after?")
                mcb.write("Is this what you were after?\n")
                yn = str(input("--> "))
                mcb.write("--> " + yn + "\n")
                while ("YES" not in yn.upper()
                       and "NO" not in yn.upper()):
                    mcb.write("Please answer 'yes' or 'no'\n")
                    print("Please answer 'yes' or 'no'")
                    yn = str(input("--> "))
                    mcb.write("--> " + yn + "\n")
                if ("YES" in yn.upper()):
                    mcb.write("Great then!\n")
                    print("Great then!")
                while ("NO" in yn.upper()):
                    if count < len(senses):
                        print('Here is another one: ')
                        mcb.write("Here is another one:\n")
                        print('> Definition: ' + senses[count].definition())
                        mcb.write('> Definition: ' + senses[count].definition()
                                  + "\n")
                        count += 1
                        print("Is this what you were after?")
                        mcb.write("Is this what you were after?\n")
                        yn = str(input("--> "))
                        mcb.write("--> " + yn + "\n")
                    else:
                        print('I know no further, sorry.')
                        mcb.write('I know no further, sorry.\n')
                        break
            ans = True
    if not ans:
        nun = random.choice(r.notu)
        gb = random.choice(r.leave)
        print(nun)
        print(gb)
        mcb.write(str(nun) + "\n")
        mcb.write(str(gb) + "\n")
    mai = random.choice(r.more)
    gb = random.choice(r.leave)
    print(mai)
    print(gb)
    mcb.write(str(mai) + "\n")
    mcb.write(str(gb) + "\n")
    reply = str(input("--> "))
    mcb.write("--> " + reply + "\n")

print("==================== PROGRAM TERMINATED ====================")
mcb.write("==================== PROGRAM TERMINATED ====================\n")

if (len(sys.argv) == 1 and '1' in co):
    os.remove("temp.txt")

mcb.close()
