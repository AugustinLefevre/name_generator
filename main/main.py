import sys
from web_scrapper import web_scrapper

if len(sys.argv) < 1:
        print("Usage: python main.py 'url'")
        sys.exit(1)
url = sys.argv[1]
print(f"url : {url}")

ws = web_scrapper()
texts = ws.scrap(url)