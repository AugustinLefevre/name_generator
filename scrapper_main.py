import csv
import os
import sys
from data_access.data_access_csv import data_access_csv
from web_scrapper.web_scrapper import web_scrapper
from named_entity_reconizer.named_entity_reconizer import named_entity_reconizer
from named_entity_reconizer.NER_CSV_storage import NER_CSV_storage

data_access = data_access_csv()
urls_file_name = "ressources/urls.csv"
ner = named_entity_reconizer()
#storage = NER_CSV_storage("target/NamedEntities.csv")

firstname_occurrence_file_name = "target/firstnameOccurrence.csv"

if os.path.exists(firstname_occurrence_file_name):
        os.remove(firstname_occurrence_file_name)
with open(firstname_occurrence_file_name, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["firstname", "occurrence"])

name_occurrence_storage = NER_CSV_storage("target/firstnameOccurrence.csv")

rows = data_access.get_rows("ressources/urls.csv")

for row in rows:
        if (row["already_scanned"] != "true"):
                row["already_scanned"] = "true"
                url = row["url"]
                print(f"url : {url}")
                texts = web_scrapper(url).scrap_texts()
                        
                for text in texts:
                        ner.parseText(text)
                        firstnames = ner.getFirstnames()
                        lastnames = ner.getLastnames()
                        locations = ner.getLocations()
                        dict_names = ner.get_dict_names()
                        name_occurrence_storage.storeFirstnameOcurence(firstnames, dict_names)
                        #storage.storeEntities(firstnames, lastnames, locations)

with open(urls_file_name, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=["url", "already_scanned"])
        writer.writeheader() 
        writer.writerows(rows)