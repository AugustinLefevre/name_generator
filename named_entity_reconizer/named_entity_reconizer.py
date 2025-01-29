import re
import spacy

class named_entity_reconizer:
    nlpFr = spacy.load("fr_core_news_lg")
    firstNames = []
    lastNames = []
    locations = []
    exclude = {"Monsieur", "Madame", "Mademoiselle"}

    def parseText(self, text) :
        self.firstNames = []
        self.lastNames = []
        self.locations = []
        docfr = self.nlpFr(text)
        for entity in docfr.ents :
            if entity.label_ == "LOC" :
                if entity.text not in self.locations:
                    print("location : " + entity.text)
                    self.locations.append(entity.text)
            elif entity.label_ == "PER" : 
                elements = entity.text.split()
                if self.is_a_name(elements[0]):
                    print("firstname : " + elements[0])
                    self.firstNames.append(elements[0])
                if len(elements) > 1 :
                    lastnameElements = elements[1:]
                    lastname = ' '.join(lastnameElements)
                    if lastname not in self.lastNames and lastname[0].isupper() and len(lastname) > 2 and (re.match('^[a-zA-Z -]*$',lastname)): 
                        print("lastname : " + lastname)
                        self.lastNames.append(lastname)
    
    def getFirstnames(self) :
        return self.firstNames
    
    def getLastnames(self) :
        return self.lastNames
    
    def getLocations(self) :
        return self.locations
    
    def is_a_name(self, name):
        result = False
        if '-' in name:
            elements = name.split('-')
        else:
            elements = [name]
        for element in elements:
            if len(element) > 2:
                if element[0].isupper() and element[1:].islower():
                    if element not in self.exclude:
                        if (re.match('^[a-zA-Z -]*$', element)):
                            if element not in self.firstNames:
                                result = True
        return result