

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionMoteurFrame(BaseFrame):

    def __init__(self, Moteur_controller, master=None):
        super().__init__(master)
        self._Moteur_controller = Moteur_controller
        self.create_widgets()

    def create_widgets(self):

        self.M_NumSerie_entry = self.create_entry("M_NumSerie", row=0)
        self.M_Modele_entry = self.create_entry("M_Modele", row=1)

        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=4, column=1, sticky=E)
        self.cancel.grid(row=4, column=2, sticky=W)

    def valid(self):

        data = dict(M_NumSerie=self.M_NumSerie_entry.get(), M_Modele=self.M_Modele_entry.get())
        try:
            Moteur_data = self._Moteur_controller.create_Moteur(data)
            messagebox.showinfo("Success",
                                "Moteur %s %s created !" % (Moteur_data['M_NumSerie'], Moteur_data['M_Modele']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
