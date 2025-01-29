import sys
from web_scrapper.web_scrapper import web_scrapper
from named_entity_reconizer.named_entity_reconizer import named_entity_reconizer
from named_entity_reconizer.NER_CSV_storage import NER_CSV_storage

if len(sys.argv) < 1:
        print("Usage: python main.py 'url'")
        sys.exit(1)
url = sys.argv[1]
print(f"url : {url}")
texts = web_scrapper(url).scrap_texts()
ner = named_entity_reconizer()
storage = NER_CSV_storage("target/NamedEntities.csv")
name_occurrence_storage = NER_CSV_storage("target/firstnameOccurrence.csv")
for text in texts:
        ner.parseText(text)
        firstnames = ner.getFirstnames()
        lastnames = ner.getLastnames()
        locations = ner.getLocations()
        name_occurrence_storage.storeFirstnameOcurence(firstnames)
        storage.storeEntities(firstnames, lastnames, locations)