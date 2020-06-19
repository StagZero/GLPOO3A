from tkinter import Label, Button
from vue.base_frame import BaseFrame


class RobotMenuFrame(BaseFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)
        self.create_widgets()

    def create_widgets(self):
        self.title = Label(self, text="Bienvenue dans le createur de Robot")
        self.subscribe = Button(self, text="Ajouter un robot", width=30, command=self._root_frame.show_subscribe_Robot)
        self.list = Button(self, text="Liste des Robots", width=30, command=self._root_frame.show_Robots)
        self.quit = Button(self, text="QUIT", fg="red", width=30,
                           command=self.quit)
        self.title.pack(side="top")
        self.subscribe.pack()
        self.list.pack()
        self.quit.pack(side="bottom")
