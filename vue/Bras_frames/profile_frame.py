from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class ProfileBrasFrame(BaseFrame):

    def __init__(self, Bras_controller, Bras, master=None):
        super().__init__(master)
        self._Bras = Bras
        self._Bras_controller = Bras_controller
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="Profile: ")
        self.title.grid(row=0, column=0, sticky=W)

        self.B_NumSerie_entry = self.create_entry("B_NumSerie: ", text=self._Bras['B_NumSerie'],
                                                  row=1,disabled=True, columnspan=3)
        self.B_Modele_entry = self.create_entry("B_Modele: ", text=self._Bras['B_Modele'],
                                                row=2, disabled=True, columnspan=3)


        #Boutons
        self.edit_button = Button(self, text="Editer", command=self.edit)
        self.cancel_button = Button(self, text="Annuler", command=self.refresh)
        self.update_button = Button(self, text="Modifier", command=self.update)
        self.remove_button = Button(self, text="Supprimer", command=self.remove)
        self.return_button = Button(self, text="Retour", fg="red", command=self.back)
        self.return_button.grid(row=5,column=0)
        self.edit_button.grid(row=5,column=1, sticky="nsew")
        self.remove_button.grid(row=5,column=2, sticky="nsew")

    def edit(self):
        self.edit_button.grid_forget()
        self.remove_button.grid_forget()
        self.B_NumSerie_entry.config(state=NORMAL)
        self.B_Modele_entry.config(state=NORMAL)
        self.cancel_button.grid(row=5, column=2, sticky="nsew")
        self.update_button.grid(row=5, column=1, sticky="nsew")

    def refresh(self):
        # Restaurer la fenêtre avec la valeur du membre et annuler l'édition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self.B_NumSerie_entry.delete(0, END)
        self.B_NumSerie_entry.insert(0, self._Bras['B_NumSerie'])
        self.B_NumSerie_entry.config(state=DISABLED)
        self.B_Modele_entry.delete(0, END)
        self.B_Modele_entry.insert(0, self._Bras['B_Modele'])
        self.B_Modele_entry.config(state=DISABLED)
        self.edit_button.grid(row=5, column=1, sticky="nsew")
        self.remove_button.grid(row=5, column=2, sticky="nsew")

    def update(self):

        data = dict(B_NumSerie=self.B_NumSerie_entry.get(), B_Modele=self.B_Modele_entry.get())
        Bras = self._Bras_controller.update_Bras(self._Bras['id'], data)
        self._Bras = Bras
        self.refresh()

    def remove(self):
        Bras_id = self._Bras['id']
        self._Bras_controller.delete_Bras(Bras_id)
        # afficher la confirmation
        messagebox.showinfo("Success",
                            "Bras %s %s deleted !" % (self._Bras['B_NumSerie'], self._Bras['B_Modele']))
        self.back()
