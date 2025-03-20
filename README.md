## setup env
python 3.10.6
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download fr_core_news_lg

pip install -U urllib3 
pip install -U brotlipy

run test with C:\name_generator> py .\run_tests.py 

## Pour récupérer une bibliotheque d'entrainement:
Le projet contient un web scrapper permettant de parcourir des sites web afin d'en extraire des nom propre.
La liste des url a parcourir ce trouve dans le fichier \resources\urls.csv
Les noms sont reconnu via un model NER (Named Entity Reconizer) et doivent donc etre contenue des phrases.
Pour executer le web scrapper des urls doivent etre presente dans le fichier correspondant puis le fichier \name_generator\scrapper_main.py doit etre lancé.
Apres l'execution les nom sont stocké temporairement dans le fichier \target\firstname occurence.

vous pouvez lancer le script C:\name_generator> py .\learn\enrich_excluded_words.py afin de valider ou non les noms

Finalement lancer le script \named_entity_reconizer\save_firstnames.py

les nom finaux sont sauvegardé dans le fichier \target\fistnames.csv


## Evolution a venir:

-lister et checker les sites deja parcouru

-rendre l'executions des scripts d'apres parsing automatique

-checker si les noms sont deja enregistre avant la demande de validation
