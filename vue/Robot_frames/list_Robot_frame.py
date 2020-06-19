
from tkinter import *

from vue.base_frame import BaseFrame


class ListRobotFrame(BaseFrame):

    def __init__(self, Robot_controller, root_frame):
        super().__init__(root_frame)
        self._Robot_controller = Robot_controller
        self._create_widgets()
        self._Robots = None

    def _create_widgets(self):

        self.title = Label(self, text="Liste des Robots:")
        self.title.grid(row=0, column=0)

        #grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        #Bouton Retour
        self.show_profile = Button(self, text="Afficher Le Robot", command=self.show_profile)
        self.menu = Button(self, text="Retour", fg="red", command=self.show_menu)
        self.menu.grid(row=4, column=0, sticky="w")

    def onselect(self, event):
        index = int(self.listbox.curselection()[0])
        print("Selection",self._Robots[index])
        self.show_profile.grid(row=4,column=0)

    def show_profile(self):
        index = int(self.listbox.curselection()[0])
        robot = self._Robots[index]
        self._root_frame.show_Robot_profile(robot['id'])

    def show(self):
        self._Robots = self._Robot_controller.list_Robot()
        self.listbox.delete(0,END)
        for index, robot in enumerate(self._Robots):
            text = robot['R_Nom'].capitalize() + ' ' + robot['MC_ID']
            self.listbox.insert(index, text)
        super().show()
