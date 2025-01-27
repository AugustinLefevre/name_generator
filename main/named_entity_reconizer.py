import spacy

class named_entity_reconizer:
    nlpFr = spacy.load("fr_core_news_sm")
    firstNames = []
    lastNames = []
    locations = []
    articles = {"le", "la", "les", "l'", "un", "une", "des"}

    def parseText(self, text) :
        self.firstNames = []
        self.lastNames = []
        self.locations = []
        docfr = self.nlpFr(text)
        for entity in docfr.ents :
            print(entity.text + " / " + entity.label_)
            if entity.label_ == "LOC" :
                if entity.text not in self.locations:
                    print("location : " + entity.text)
                    self.locations.append(entity.text)
            elif entity.label_ == "PER" : 
                elements = entity.text.split()
                if elements[0] not in self.firstNames:
                    print("firstname : " + elements[0])
                    self.firstNames.append(elements[0])
                if len(elements) > 1 :
                    lastnameElements = elements[1:]
                    lastname = ' '.join(lastnameElements)
                    if lastname not in self.lastNames : 
                        print("lastname : " + lastname)
                        self.lastNames.append(lastname)
    
    def getFistNames(self) :
        return self.firstNames
    
    def getLastNames(self) :
        return self.lastNames
    
    def getLocations(self) :
        return self.locations