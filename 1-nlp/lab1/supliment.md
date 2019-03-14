# Temă supliment
## Identificator: `python_siruri_general_`

In paranteza, vi se indica eventualele functii dintre care puteti alege pentru rezolvarea subpunctelor de mai jos.

Se da un sir de caractere cuprinzand un paragraf. De exemplu:
> "Candva, demult, acum 1000 de ani traia o printesa intr-un castel. Si printesa intr-o zi auzi cum aparuse pe meleagurile sale un cufar fermecat din care iesea grai omenesc. Printesa curioasa strabatu 7 ulite si 7 piete; ajunse la cufar si vazu ca toti stateau la 100 metri distanta de el si se mirau. Din cufar intr-adevar se auzeau vorbe nedeslusite. Printesa curajoasa se duse sa-i vorbeasca. Il intreba cine e si ce dorinte are. Raspunsul fu: \"Sunt Ion am cazut in cufar si m-am ferecat din gresala. As dori sa ies.\". Printesa deschise cufarul si-l elibera pe Ion. "Multumesc" spuse Ion. Si astfel, povestea cufarului fermecat a fost deslusita.".

Subpunctele de mai jos trebuie rezolvate fara a depinde de continutul textului (sa se poate oferi si alt text si programul sa functioneze in continuare).

1. (`len`) Sa se afiseze cate caractere are sirul.
2. (`isalpha/isdigit/isalnum`) Scrieti o functie care primeste ca parametru un sir si calculeaza lista cu toate caracterele nealfanumerice care apar in sir, cu exceptia cratimei.
3. (`split`, eventual `strip`)Cu ajutorul listei de caractere nealfanumerice de mai sus, se sa se obtina lista cu cuvintele (in lowercase) din paragraf. Consieram un singur cuvant si un sir cu cratima. Sirurile nu trebuie sa contina si spatiile din jurul cuvintelor.
4. (`starsWith/endsWith`)Sa se identifice potentialele cuvinte (substantive/numerale) articulate de gen masculin (care se termina in "ul")
5. (`find`)Sa se obtina lista sirurilor cu cratima

*Observatie*: subpunctele au punctaje diferite.
**Punctaj**: 0.1


## Identificator: `python_liste_general_`
Consideram lista 
```python
l=["margareta", "crizantema","lalea"," zorea , violeta, orhidee","trandafir","gerbera , iasomie","iris","crin "]
```

1. (**adaugare/stergere**) Sa se scrie o functie care citeste un cuvant de la tastatura, si, daca acesta exista in lista, e sters din pozitia curenta si mutat la final, iar daca nu exista, pur si simplu e adaugat la final. Se va apela functia si se va afisa rezultatul.
2. (**inlocuire secventa in lista**) Scrieti o secventa de cod care sa inlocuiasca toate elementele de tip sir continand mai multe nume de flori separate prin virgula, punand in loc numele de flori ca elemente (si eliminand si spatiile in plus). De exemplu din `["a","b, c, d","e"]` rezulta `["a","b","c","d","e"]`. Lista rezultata va fi pusa in variabila l si se va afisa.
3. (**creare lista**) Sa se scrie o functie care primeste un caracter si lista de cuvinte l si returneaza o lista noua doar cu cuvintele ce contin acel caracter. Se va apela functia si se va afisa rezultatul.
4. (**sortare lista/reverse**) Sa sorteze si afiseze lista de cuvinte in ordine alfabetica si invers alfabetica. Folositi sort si reverse.

*Observatie*: subpunctele au punctaje diferite.
**Punctaj**: 0.1

## Identificator: `python_matrici_general_`

Se da o lista de cuvinte (de exemplu: `["papagal", "pisica","soarece","bolovan","soparla","catel", "pasare"]`).

1. (**generare matrice, adaugare de elemente**) Sa se scrie o functie `gen_matrice()` Functia genereaza (indiferent de susbsetul de litere folosite in cuvinte) matricea avand liniile si coloanele corespunzatoare tuturor literelor din alfabet (pentru simplitate folosim alfabetul englezesc - deci fara caractere Unicode speciale precum litere cu diacritice). Prima linie si prima coloana vor contine chiar litere alfabetului in ordine, restul matricii va fi completatv cu 0.
2. (**modificare matrice**) Sa se scrie o alta functie, `completeaza_matrice()`, care primeste ca parametru lista de cuvinte si matricea creata mai devreme. Functia va modifa matricea astfel incat un element de pe pozitia i+1,j+1 reprezinta numarul de dati in care litera corespunzatoare liniei i s-a aflat intr-un cuvant in urma literei corespunzatoare coloanei j. Se va apela functia si se va afisa matricea.
3. (**eliminare de linii si coloane**) Sa se elimine din matrice liniile si coloanele cu toate elementele 0. Sa se afiseze matricea.
4. (**parcurgere matrice**) Sa se afiseze perechile (distincte) de litere cu numarul de aparitii mai mare sau egal decat un N (dati voi o valoare, de exemplu 2.

*Observatie*: subpunctele au punctaje diferite.
**Punctaj**: 0.1.

## Identificator: `python_dictionare_general_`

Se da o lista de siruri despartite ( in silabe sau alte tipuri de parti, prin cratima), de exemplu: 
```python
[
    "co-pa-cel", "pa-pu-cel","a-bac","021-220-20-10","1-pi-tic",
    "go-go-nea","tip-til","123-456","a-co-lo","lo-go-ped",
    "pa-pa-gal","co-co-starc"
]
```

1. (**creare dictionar**) Creati un dictionar (enumerandu-i elementele) cu cheile si valorile urmatoare (grupate in paranteze, unde primul element e cheia si al doilea e valoarea): `("vocale","aeiou"), ("consoane", "bcdfghjklmnpqrstvxyz"), 
("cifre","0123456789")`
2. (**adaugare in dictionar**) Sa se calculeze un dictionar pe baza listei de siruri, unde cheile sunt partile de cuvant iar valoarea corespunzatoare pentru fiecare cheie o reprezinta lista cu cuvintele care contin acea parte de cuvant)
3. (**stergere elem din dictionar**) Din dictionarul rezultat sa se elimine cheile formate din cifre (si sa se afiseze perechile de cheie-valoare eliminate).
4. (**lungime dictionar**) Sa se afiseze cate chei au mai ramas in dictionar
5. (**parcurgere chei/valori**) Sa se calculeze si afiseze lista cu silabele de forma consoana-vocala-consoana.

**Punctaj**: 0.1
