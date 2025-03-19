import re
import spacy

class named_entity_reconizer:
    nlpFr = spacy.load("fr_core_news_lg")
    firstNames = []
    lastNames = []
    locations = []
    dict_names = {}
    
    excluded_words_file = "ressources/excluded_words.csv"

    excludeds = []

    with open(excluded_words_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["excluded"] != ""):
                    excludeds.append(row["excluded"])

    def parseText(self, text) :
        self.firstNames = []
        self.lastNames = []
        self.locations = []
        lines = text.splitlines()
        for line in lines:
            docfr = self.nlpFr(line)
            propn = [token.text for token in docfr if token.pos_ == "PROPN"]
            for entity in docfr.ents :
                if entity.label_ == "LOC" :
                    if entity.text not in self.locations:
                        self.locations.append(entity.text)
                elif entity.label_ == "PER" : 
                    elements = entity.text.split()
                    firstname = elements[0]
                    if (re.match('^[a-zA-Z -]*$', firstname)):
                        compound_noun = firstname.split('-')
                        if len(compound_noun) <= 2:
                            for name in compound_noun:
                                if self.is_a_name(name, line):
                                    print("firstname : " + name)
                                    self.firstNames.append(name)
                                    self.dict_names[name] = line
                        if len(elements) > 1 :
                            lastnameElements = elements[1:]
                            lastname = ' '.join(lastnameElements)
                            if lastname not in self.lastNames and lastname[0].isupper() and len(lastname) > 2 and (re.match('^[a-zA-Z -]*$',lastname)): 
                                self.lastNames.append(lastname)
    
    def getFirstnames(self) :
        return self.firstNames
    
    def getLastnames(self) :
        return self.lastNames
    
    def getLocations(self) :
        return self.locations
    
    def get_dict_names(self) :
        return self.dict_names
    
    def is_a_name(self, name, source_text):
        if name == source_text :
            return False

        excluded_previous_tokens = ["le", "les", "la", "du", "des"]
        excluded_next_tokens = ["à", "aux"]
        previous_word = self.get_previous_word(name, source_text)
        next_word = self.get_next_word(name, source_text)
        if(previous_word.lower() in excluded_previous_tokens) or next_word.lower() in excluded_next_tokens:
            return False
        
        if len(name) == 3:
            if not name.isalpha():
                return False
            vowel_nb = self.count_vowels(name)
            if vowel_nb <= 1 and not self.is_vowel(name[1]):
                return False

        if len(name) > 2:
            if name[0].isupper() and name[1:].islower():
                if name not in self.excludeds:
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
    
    def get_previous_word(self, actual_token, text):
        match = re.search(r"(\b\w+)\s+"+actual_token, text)
        previous_word = ""
        if match:
            previous_word = match.group(1)
        return previous_word
    
    def get_next_word(self, actual_token, text):
        regex = re.escape(actual_token) + r"\s+(\w+)" 
        match = re.search(regex, text)
        next_word = ""
        if match:
            next_word = match.group(1)
        return next_word
