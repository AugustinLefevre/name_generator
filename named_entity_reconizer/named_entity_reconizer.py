import re
import spacy

class named_entity_reconizer:
    nlpFr = spacy.load("fr_core_news_lg")
    firstNames = []
    lastNames = []
    locations = []
    exclude = {"Monsieur",
               "Messieurs",
               "Madame",
               "Mesdames",
               "Mademoiselle",
               "Docteur",
               "Doctor",
               "Maitre",
               "Sir",
               "Sire"}

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
                firstname = elements[0]
                if (re.match('^[a-zA-Z -]*$', firstname)):
                    compound_noun = firstname.split('-')
                    if len(compound_noun) <= 2:
                        for name in compound_noun:
                            if self.is_a_name(name):
                                print("firstname : " + name)
                                self.firstNames.append(name)
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
        if len(name) == 3:
            if not name.isalpha():
                return False
            vowel_nb = self.count_vowels(name)
            if vowel_nb <= 1 and not self.is_vowel(name[1]):
                return False

        if len(name) > 2:
            if name[0].isupper() and name[1:].islower():
                if name not in self.exclude:
                    if (re.match('^[a-zA-Z -]*$', name)):
                        if name not in self.firstNames:
                            return True
        return False
    
    def count_vowels(self, name):
        count = 0
        for char in name:
            if self.is_vowel(char):
                count += 1
        return count
    
    def is_vowel(self, char):
        vowels = "aeiouAEIOU"
        return char in vowels
