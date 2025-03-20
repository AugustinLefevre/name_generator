import csv 

class data_access_csv:
    
    def get_rows(self, file_location):
        with open(file_location, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            rows = list(reader)
        return rows