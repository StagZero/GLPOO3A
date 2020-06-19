

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionBrasFrame(BaseFrame):

    def __init__(self, Bras_controller, master=None):
        super().__init__(master)
        self._Bras_controller = Bras_controller
        self.create_widgets()

    def create_widgets(self):

        self.B_NumSerie_entry = self.create_entry("B_NumSerie", row=0)
        self.B_Modele_entry = self.create_entry("B_Modele", row=1)

        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=4, column=1, sticky=E)
        self.cancel.grid(row=4, column=2, sticky=W)

    def valid(self):

        data = dict(B_NumSerie=self.B_NumSerie_entry.get(), B_Modele=self.B_Modele_entry.get())
        try:
            Bras_data = self._Bras_controller.create_Bras(data)
            messagebox.showinfo("Success",
                                "Bras %s %s created !" % (Bras_data['B_NumSerie'], Bras_data['B_Modele']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
