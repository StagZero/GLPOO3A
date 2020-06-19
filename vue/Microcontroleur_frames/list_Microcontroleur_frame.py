
from tkinter import *

from vue.base_frame import BaseFrame


class ListMicrocontroleurFrame(BaseFrame):

    def __init__(self, Microcontroleur_controller, root_frame):
        super().__init__(root_frame)
        self._Microcontroleur_controller = Microcontroleur_controller
        self._create_widgets()
        self._Microcontroleurs = None

    def _create_widgets(self):

        self.title = Label(self, text="Liste des Microcontroleurs:")
        self.title.grid(row=0, column=0)

        #grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=40, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        #Bouton Retour
        self.show_profile = Button(self, text="Afficher Le Microcontroleur", command=self.show_profile)
        self.menu = Button(self, text="Retour", fg="red", command=self.show_menu)
        self.menu.grid(row=4, column=0, sticky="w")

    def onselect(self, event):
        index = int(self.listbox.curselection()[0])
        print("Selection",self._Microcontroleurs[index])
        self.show_profile.grid(row=4,column=0)

    def show_profile(self):
        index = int(self.listbox.curselection()[0])
        microcontroleur = self._Microcontroleurs[index]
        self._root_frame.show_Microcontroleur_profile(microcontroleur['id'])

    def show(self):
        self._Microcontroleurs = self._Microcontroleur_controller.list_Microcontroleur()
        self.listbox.delete(0,END)
        for index, microcontroleur in enumerate(self._Microcontroleurs):
            text = microcontroleur['MC_NumSerie'].capitalize() + ' ' + microcontroleur['MC_Modele'].capitalize() + ' ' + microcontroleur['MC_Etat'].capitalize() + ' ' + microcontroleur['M_ID'] + ' ' + microcontroleur['B_ID']
            self.listbox.insert(index, text)
        super().show()
