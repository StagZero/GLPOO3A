
from tkinter import *

from vue.base_frame import BaseFrame


class ListRobotFrame(BaseFrame):

    def __init__(self, Robot_controller, Microcontroleur_controller, root_frame):
        super().__init__(root_frame)
        self._Robot_controller = Robot_controller
        self._Microcontroleur_controller = Microcontroleur_controller
        self._create_widgets()
        self._Robots = None

    def _create_widgets(self):

        self.title = Label(self, text="Liste des Robots:")
        self.title.grid(row=0, column=0)

        #grille
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=40, selectmode='single')
        yDefil['command'] = self.listbox.yview
        self.listbox.bind('<<ListboxSelect>>', self.onselect)
        yDefil.grid(row=1, column=1, sticky='ns')
        self.listbox.grid(row=1, column=0, sticky='nsew')

        #Bouton Retour
        self.start_action = Button(self, text="Démarrer le Robot" , command=self.start_action)
        self.show_profile = Button(self, text="Afficher Le Robot", command=self.show_profile)
        self.menu = Button(self, text="Retour", fg="red", command=self.show_menu)
        self.menu.grid(row=4, column=0, sticky="w")

    def onselect(self, event):
        index = int(self.listbox.curselection()[0])
        print("Selection",self._Robots[index])
        self.show_profile.grid(row=4,column=0)
        self.start_action.grid(row=4, column=1)

    def show_profile(self):
        index = int(self.listbox.curselection()[0])
        robot = self._Robots[index]
        self._root_frame.show_Robot_profile(robot['id'])

    def show(self):
        self._Robots = self._Robot_controller.list_Robot()
        self.listbox.delete(0,END)
        for index, robot in enumerate(self._Robots):
            mc = self._Microcontroleur_controller.get_Microcontroleur(robot['MC_ID'])
            text = robot['R_Nom'].capitalize() + ' ' + mc['MC_NumSerie']
            self.listbox.insert(index, text)
        super().show()

    def start_action(self):
        index = int(self.listbox.curselection()[0])
        robot = self._Robots[index]
        self._Robot_controller.start(robot['id'])
