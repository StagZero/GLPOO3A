from tkinter import Label, Button
from vue.base_frame import BaseFrame


class MicrocontroleurMenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Bienvenue dans le createur de Microcontroleur")
        self.subscribe = Button(self, text="Ajouter un Microcontroleur", width=30, command=self._root_frame.show_subscribe_Microcontroleur)
        self.list = Button(self, text="Liste des Microcontroleurs", width=30, command=self._root_frame.show_Microcontroleurs)
        
        self.title.pack(side="top")
        self.subscribe.pack()
        self.list.pack()
        
