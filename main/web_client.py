
import requests
import brotli
import zlib
from io import BytesIO
import gzip

class web_client():
    header = ""
    url = ""

    def set_header(self, header):
        self.header = header
        return self

    def set_url(self, url):
        self.url = url
        return self
    
    def get_response(self):
        
        self.response = requests.get(self.url, headers=self.header)
        return self.response
    
    def is_compressed(self, content_encoding):
        return content_encoding in ['br', 'gzip', 'deflate']
    
    def get_content(self):
        self.response = requests.get(self.url, headers=self.header)
        if self.response.status_code != 200:
            print(f"\033[91m Error {self.response.status_code} request {self.url}\033[00m")

        if not self.is_compressed(self.response):
            return self.response.content.decode(self.response.encoding)
        
        content_encoding = self.response.headers.get('Content-Encoding', '').lower()
        compressed_content = self.response.content

        try:
            if 'br' in content_encoding:
                print("Décompression avec Brotli...")
                decompressed_content = brotli.decompress(compressed_content)
            elif 'gzip' in content_encoding:
                print("Décompression avec Gzip...")
                with gzip.GzipFile(fileobj=BytesIO(compressed_content)) as gz:
                    decompressed_content = gz.read()
            elif 'deflate' in content_encoding:
                print("Décompression avec Deflate...")
                decompressed_content = zlib.decompress(compressed_content)
            else:
                print("Pas de compression détectée...")
                decompressed_content = compressed_content
        except brotli.error as e:
            print(f"Erreur lors de la décompression Brotli: {e}")
            return None

        return decompressed_content.decode(self.response.encoding)
    
    
