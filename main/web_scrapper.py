
import os

from urllib.parse import urlparse, urljoin
from web_client import web_client
from bs4 import BeautifulSoup

class web_scrapper:
    def __init__(self, url):
        self.url = url
        self.visited_links = set()
        self.limit = 1000
        self.web_client = web_client()
        self.web_client.set_header({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Connection': 'keep-alive'
            })

    def get_texts(self, url, tags=['p']):
        try:
            
            html = self.web_client.set_url(url).get_content()
            
            soup = BeautifulSoup(html, "html.parser")

            extracted_text = []
            for tag in tags:
                elements = soup.find_all(tag)
                for element in elements:
                    extracted_text.append(element.get_text())

            final_text = " ".join(extracted_text)
            return extracted_text
        except Exception as e:
            print(f"Error fetching texts from {url}: {e}")
            return ""

    def get_links(self):
        
        try:
            html = self.web_client.set_url(self.url).get_content()
            soup = BeautifulSoup(html, "html.parser")
            
            extracted_links = []
            tags = ['a']

            for tag in tags:
                elements = soup.find_all(tag)
                
                for element in elements:
                    href = element.get('href')
                    if href:
                        full_url = urljoin(self.url, href)
                        if self.url in full_url:
                            extracted_links.append(full_url)
            return extracted_links
        except Exception as e:
            print(f"\033[91m Error fetching links from {self.url}: {e}\033[00m")
            return []

    def scan_site_map(self, url):
        links = self.get_links()
        for link in links:
            if self.limit > len(self.visited_links) and link not in self.visited_links:
                print(f"\033[92m {link}\033[00m")
                self.visited_links.add(link)
                self.scan_site_map(url)
        return list(self.visited_links)
    
    def scrap_texts(self):
        urls = self.scan_site_map(self.url)
        texts = []

        for url in urls:
            texts = texts + self.get_texts(url)
        return texts
