

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionRobotFrame(BaseFrame):

    def __init__(self, Robot_controller, master=None):
        super().__init__(master)
        self._Robot_controller = Robot_controller
        self.create_widgets()

    def create_widgets(self):

        self.R_Nom_entry = self.create_entry("R_Nom", row=0)
        self.MC_ID_entry = self.create_entry("MC_ID", row=1)

        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=4, column=1, sticky=E)
        self.cancel.grid(row=4, column=2, sticky=W)

    def valid(self):

        data = dict(R_Nom=self.R_Nom_entry.get(), MC_ID=self.MC_ID_entry.get())
        try:
            Robot_data = self._Robot_controller.create_Robot(data)
            messagebox.showinfo("Success",
                                "Robot %s %s created !" % (Robot_data['R_Nom'], Robot_data['MC_ID']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
