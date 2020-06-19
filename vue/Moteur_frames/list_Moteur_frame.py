
from tkinter import *

from vue.base_frame import BaseFrame


class ListMoteurFrame(BaseFrame):

    def __init__(self, Moteur_controller, root_frame):
        super().__init__(root_frame)
        self._Moteur_controller = Moteur_controller
        self._create_widgets()
        self._Moteurs = None

    def _create_widgets(self):

        self.title = Label(self, text="Liste des Moteurs:")
        self.title.grid(row=0, column=0)

        #grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        #Bouton Retour
        self.show_profile = Button(self, text="Afficher Le Moteur", command=self.show_profile)
        self.menu = Button(self, text="Retour", fg="red", command=self.show_menu)
        self.menu.grid(row=4, column=0, sticky="w")

    def onselect(self, event):
        index = int(self.listbox.curselection()[0])
        print("Selection",self._Moteurs[index])
        self.show_profile.grid(row=4,column=0)

    def show_profile(self):
        index = int(self.listbox.curselection()[0])
        moteur = self._Moteurs[index]
        self._root_frame.show_Moteur_profile(moteur['id'])

    def show(self):
        self._Moteurs = self._Moteur_controller.list_Moteur()
        self.listbox.delete(0,END)
        for index, moteur in enumerate(self._Moteurs):
            text = moteur['M_NumSerie'].capitalize() + ' ' + moteur['M_Modele'].capitalize()
            self.listbox.insert(index, text)
        super().show()
