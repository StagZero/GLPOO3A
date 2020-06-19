

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionMicrocontroleurFrame(BaseFrame):

    def __init__(self, Microcontroleur_controller, master=None):
        super().__init__(master)
        self._Microcontroleur_controller = Microcontroleur_controller
        self.create_widgets()

    def create_widgets(self):

        self.MC_NumSerie_entry = self.create_entry("MC_NumSerie", row=0)
        self.MC_Modele_entry = self.create_entry("MC_Modele", row=1)
        self.MC_Etat_entry = self.create_entry("MC_Etat", row=2)
        self.M_ID_entry = self.create_entry("M_ID", row=3)
        self.B_ID_entry = self.create_entry("B_ID", row=4)


        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=5, column=1, sticky=E)
        self.cancel.grid(row=5, column=2, sticky=W)

    def valid(self):

        data = dict(MC_NumSerie=self.MC_NumSerie_entry.get(), MC_Modele=self.MC_Modele_entry.get(), MC_Etat=self.MC_Etat_entry.get(), M_ID=self.M_ID_entry.get(), B_ID=self.B_ID_entry.get())
        try:
            Microcontroleur_data = self._Microcontroleur_controller.create_Microcontroleur(data)
            messagebox.showinfo("Success",
                                "Microcontroleur %s %s created !" % (Microcontroleur_data['MC_NumSerie'], Microcontroleur_data['MC_Modele']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
