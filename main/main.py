import sys
from web_scrapper import web_scrapper
from named_entity_reconizer import named_entity_reconizer
from NER_CSV_storage import NER_CSV_storage

if len(sys.argv) < 1:
        print("Usage: python main.py 'url'")
        sys.exit(1)
url = sys.argv[1]
print(f"url : {url}")
texts = web_scrapper(url).scrap_texts()
ner = named_entity_reconizer()
storage = NER_CSV_storage("../target/NamedEntities.csv")
for text in texts:
        ner.parseText(text)
        firstnames = ner.getFirstnames()
        lastnames = ner.getLastnames()
        locations = ner.getLocations()
        storage.storeEntities(firstnames, lastnames, locations)