import csv
from data_access.data_access_csv import data_access_csv

class NER_CSV_storage :
    outputFile = ""
    data_access = data_access_csv()

    def __init__(self, outputFileName):
        self.outputFile = outputFileName

    def storeFirstnameOcurence(self, firstnames, name_source):
        firstnames_occurences = self.data_access.get_rows(self.outputFile)

        for firstname in firstnames:
            found = False
            for entry in firstnames_occurences:
                if entry["firstname"] == firstname:
                    entry["occurrence"] = int(entry["occurrence"]) + 1
                    entry["source"] = name_source[firstname]
                    found = True
                    break
            if not found:
                firstnames_occurences.append({"firstname" : firstname, "occurrence" : 1, "source" : name_source[firstname]})
            

        self.data_access.overwrite(self.outputFile, firstnames_occurences)



        


