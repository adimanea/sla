# MathChatBot

This is a project that I chose as final homework for the NLP laboratory at the Security and Applied Logic Master's program at the University of Bucharest.

## Description
The project implements a (rudimentary) chatbot which (tries to) hold a conversation with you on mathematical topics. It will give you definitions of mathematical objects, ask you to study or to practice doing some exercises... y'know, nagging professor stuff.

## How to run it
Open a terminal and run Python 3 on the file, specifying the output text file for logging.

Example:

``` shell
python3 mcb.py log.txt
```

Then the conversation will take place in the terminal and the transcript will be available in `log.txt`.

If the program is not run with the output file argument, you will have the choice to add it or continue without it or exit.

## How does it work?
The program uses the `WordNet` database for all the words and definitions, as well as the `Stanford POS Tagger` for parsing phrases.

The bot greets you and asks you what do you want to learn (or talk) about.

- It has a database consisting of a list of synsets for mathematical terms. 
- It also has a database of specific verbs (e.g. *learn*, *study*, *exercise*, *practice*, *define*).
- It parses the line you enter, looking especially for *nouns* and *verbs* (rather, noun phrases and verbal phrases), as tagged by the Stanford POS Tagger.
- For each noun it found, it will make a list of similarity scores of it with respect to the nouns in the database, which will be sorted, to choose the one that is most relevant.
- For each verb it found, it will look it up in the database.
- Corresponding to the VP and NP, it will offer predefined answers.
- If you are trying to define a polysemantic noun, it will offer all the definitions it has, until you are happy with them.

## Example conversation
> === mcb.py === <br />
> === Fri Dec 28 11:29:15 2018 === <br />
> Hi, how can I help you today? <br />
> Here are the topics I know something about: <br />
> group <br />
> limit <br />
> sum <br />
> product <br />
> integral <br />
> derivative <br />
> differential <br />
> exponential <br />
> logarithm <br />
> fraction <br />
> calculus <br />
> analysis <br />
> I can help you { study, learn, practice, read, exercise, define } some of these. <br />
> You can always end the conversation saying goodbye. <br />
> --> define group <br />
> I can give you the definition of group. <br />
> I know 2 definitions of group. <br />
> Here is one of them: <br />
> > Definition: any number of entities (members) considered as a unit <br />
> Is this what you were after? <br />
> --> yes <br />
> Great then! <br />
> What else do you want to talk about? <br />
> You can always end the conversation saying goodbye. <br />
> --> practice derivatives <br />
> Practice makes perfect, you know? <br />
> First, read the theory, then try solving some exercises in the textbook. See how that works for you. <br />
> What else do you want to talk about? <br />
> You can always end the conversation saying goodbye. <br />
> --> learn calculus <br />
> So, you want to learn about calculus or something related. <br />
> You can get together with some colleagues and try studying through discussions and debates if that works for you. <br />
> What else do you want to talk about? <br />
> You can always end the conversation saying goodbye. <br />
> --> I want to study products <br />
> So, you want to learn about intersection or something related. <br />
> Reading your course notes is always a good start. <br />
> What else do you want to talk about? <br />
> You can always end the conversation saying goodbye. <br />
> --> bye <br />


## Further features (F) and ideas (I)
- (I) The bot will provide clickable links by querying `DuckDuckGo !w` for what you want to learn about.
- (I) Add more terms, verbs and senses.

## Known issues
- Sometimes, the name of a noun does not correspond to what you entered. For example, for `sum`, it will also include `union`, so although `sum` is polysemantic, if it chooses `union`, it will not give you more senses. This can be fixed by disambiguating and/or checking more carefully for names and lemmas.


## Tools used
- NLTK, Stanford POS Tagger, WordNet in Python 3;
- Emacs, Vim, st, GitLab.


## Other credits
- I learned to use the tools with the help of the [NLP Lab](http://irinaciocan.ro/proces_lbnat/) (in Romanian) taught by Mrs. Irina Ciocan.
- Inspired by [ELIZA](https://en.wikipedia.org/wiki/ELIZA), see Common Lisp code [here](http://norvig.com/paip/eliza.lisp).
