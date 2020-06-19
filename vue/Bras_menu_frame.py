from tkinter import Label, Button
from vue.base_frame import BaseFrame


class BrasMenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Bienvenue dans le createur de Bras")
        self.subscribe = Button(self, text="Ajouter un bras", width=30, command=self._root_frame.show_subscribe_Bras)
        self.list = Button(self, text="Liste des Bras", width=30, command=self._root_frame.show_Brass)
        
        self.title.pack(side="top")
        self.subscribe.pack()
        self.list.pack()
        
