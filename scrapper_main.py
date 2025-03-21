from data_access.data_access_csv import data_access_csv
from web_scrapper.web_scrapper import web_scrapper
from named_entity_reconizer.named_entity_reconizer import named_entity_reconizer
from named_entity_reconizer.NER_CSV_storage import NER_CSV_storage

data_access = data_access_csv()
urls_file_location = "ressources/urls.csv"
ner = named_entity_reconizer()

firstname_occurrence_file_name = "target/firstnameOccurrence.csv"

name_occurrence_storage = NER_CSV_storage(firstname_occurrence_file_name)

rows = data_access.get_rows(urls_file_location)

for row in rows:
        if (row["already_scanned"] != "true"):
                row["already_scanned"] = "true"
                url = row["url"]
                print(f"url : {url}")
                texts = web_scrapper(url).scrap_texts()
                        
                for text in texts:
                        ner.parseText(text)
                        firstnames = ner.getFirstnames()
                        dict_names = ner.get_dict_names()
                        name_occurrence_storage.storeFirstnameOcurence(firstnames, dict_names)

data_access.overwrite(urls_file_location, rows)