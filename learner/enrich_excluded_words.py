from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import csv

class MonInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        # Liste des chaînes de caractères
        outputFile = "target/firstnameOccurrence.csv"

        self.names = []

        with open(outputFile, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["firstname"] != ""):
                    self.names.append(row["firstname"])

        excluded_words_file = "ressources/excluded_words.csv"

        self.excludeds = []

        with open(excluded_words_file, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile) 
            for row in reader:
                if(row["excluded"] != ""):
                    self.excludeds.append(row["excluded"])



        self.index = 0  # Indice actuel de la liste

        # Label pour afficher le texte
        self.label = Label(text=self.names[self.index], font_size=200)
        self.add_widget(self.label)

        # Bouton pour changer de texte
        self.bouton_yes = Button(text="True", size_hint=(1, 0.2))
        self.bouton_yes.bind(on_press=self.approve)
        self.add_widget(self.bouton_yes)

        self.bouton_no = Button(text="False", size_hint=(1, 0.2))
        self.bouton_no.bind(on_press=self.disapprove)
        self.add_widget(self.bouton_no)

    def approve(self, instance):
        """ Change le texte affiché au prochain élément de la liste """
        if self.index < len(self.names) - 1:
            self.index += 1
            self.label.text = self.names[self.index]
        else:
            self.label.text = "Fin de la liste"

    def disapprove(self, instance):
        outputFile = "ressources/excluded_words.csv"
        if(self.names[self.index] not in self.excludeds) :
            with open(outputFile, mode="a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([self.names[self.index]])
        if self.index < len(self.names) - 1:
            self.index += 1
            self.label.text = self.names[self.index]
        else:
            self.label.text = "Fin de la liste"

class MonApp(App):
    def build(self):
        return MonInterface()

if __name__ == "__main__":
    MonApp().run()
