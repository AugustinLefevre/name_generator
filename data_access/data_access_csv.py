import csv 

class data_access_csv:
    
    def get_rows(self, file_location):
        with open(file_location, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            rows = list(reader)
        return rows
    
    def get_headers(self, file_location):
        with open(file_location, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
        return headers
    
    def overwrite(self, file_location, rows):
        headers = self.get_headers(file_location)
        with open(file_location, mode="w", newline="", encoding="utf-8") as fichier:
            writer = csv.DictWriter(fichier, fieldnames=headers)
            writer.writeheader() 
            writer.writerows(rows)

    def get_column(self, file_location, column):
        if(column not in self.get_headers(file_location)):
            print(f"\033[91m Error column name invalid\033[00m")
        rows = self.get_rows(file_location)
        result = [d[column] for d in rows]
        return result