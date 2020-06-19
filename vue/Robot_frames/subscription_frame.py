

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error
from controller.Microcontroleur_controller import MicrocontroleurController

class SubscriptionRobotFrame(BaseFrame):

    def __init__(self, Robot_controller,Microcontroleur_controller, master=None):
        super().__init__(master)
        self._Robot_controller = Robot_controller
        self._Microcontroleur_controller = Microcontroleur_controller
        self._MCs= None
        self._MC = None
        self.create_widgets()

    def create_widgets(self):

        self.R_Nom_entry = self.create_entry("R_Nom", row=0)
        NON = Label(self,text="MC_ID")
        NON.grid(row=3)
        self._MCs = self._Microcontroleur_controller.list_Microcontroleur()
        listrandom1=[]
        for index, mcs in enumerate(self._MCs):
            text = mcs['MC_NumSerie']
            listrandom1.insert(index, text)
        self.M_ID_entry = ttk.Combobox(self,value=listrandom1)
        self.M_ID_entry.grid(row=3,column=1)

        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=4, column=1, sticky=E)
        self.cancel.grid(row=4, column=2, sticky=W)

    def valid(self):
        self._MC = self._Microcontroleur_controller.search_Microcontroleur(self.M_ID_entry.get())

        data = dict(R_Nom=self.R_Nom_entry.get(), MC_ID=self._MC['id'])
        try:
            Robot_data = self._Robot_controller.create_Robot(data)
            messagebox.showinfo("Success",
                                "Robot %s %s created !" % (Robot_data['R_Nom'], Robot_data['MC_ID']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
