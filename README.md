## setup env
python 3.10.6
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download fr_core_news_lg

pip install -U urllib3 
pip install -U brotlipy

run test with C:\name_generator> py .\run_tests.py 

## Pour récupérer une bibliotheque d'entrainement:
Le projet contient un web scrapper permettant de parcourir des sites web afin d'en extraire des noms propres.
La liste des url à parcourir ce trouve dans le fichier \resources\urls.csv
Les noms sont reconnus via un model NER (Named Entity Reconizer) et doivent donc etre contenue dans des phrases afin que le traitement soit optimisé.
Pour executer le web scrapper des urls doivent etre presente dans le fichier correspondant puis le fichier \name_generator\scrapper_main.py doit etre lancé.
Apres l'execution les noms sont stockés temporairement dans le fichier \target\firstname occurence.

Vous pouvez lancer le script C:\name_generator> py .\learn\enrich_excluded_words.py afin de valider ou non les noms

Finalement, lancer le script \named_entity_reconizer\save_firstnames.py

les nom finaux sont sauvegardés dans le fichier \target\fistnames.csv


## Evolution a venir:

-rendre l'executions des scripts d'apres parsing automatique

-inverser la dependance a cvs
