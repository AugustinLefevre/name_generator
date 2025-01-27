import csv

# columns 
class NER_CSV_storage :
    outputFile = ""

    def __init__(self, outputFileName):
        self.outputFile = outputFileName

    def storeEntities(self, firstnames, lastnames, locations) :
        column_firstname = []
        column_lastname = []
        column_location = []

        with open(self.outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["firstname"] != ""):
                    column_firstname.append(row["firstname"])
                if(row["lastname"] != ""):
                    column_lastname.append(row["lastname"])
                if(row["location"] != ""):
                    column_location.append(row["location"])

        for firstname in firstnames:
            if firstname not in column_firstname:
                column_firstname.append(firstname)
        for lastname in lastnames:
            if lastname not in column_lastname:
                column_lastname.append(lastname)
        for location in locations:
            if location not in column_location:
                column_location.append(location)
    
        with open(self.outputFile, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["firstname", "lastname", "location"])

            max_length = max(len(column_firstname), len(column_lastname), len(column_location))

            column_firstname += [""] * (max_length - len(column_firstname))
            column_lastname += [""] * (max_length - len(column_lastname))
            column_location += [""] * (max_length - len(column_location))

            for first, last, loc in zip(column_firstname, column_lastname, column_location):
                writer.writerow([first, last, loc])


        


