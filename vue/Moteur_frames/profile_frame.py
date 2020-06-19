from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class ProfileMoteurFrame(BaseFrame):

    def __init__(self, Moteur_controller, Moteur, master=None):
        super().__init__(master)
        self._Moteur = Moteur
        self._Moteur_controller = Moteur_controller
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="Profile: ")
        self.title.grid(row=0, column=0, sticky=W)

        self.M_NumSerie_entry = self.create_entry("M_NumSerie: ", text=self._Moteur['M_NumSerie'],
                                                  row=1,disabled=True, columnspan=3)
        self.M_Modele_entry = self.create_entry("M_Modele: ", text=self._Moteur['M_Modele'],
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
        self.M_NumSerie_entry.config(state=NORMAL)
        self.M_Modele_entry.config(state=NORMAL)
        self.cancel_button.grid(row=5, column=2, sticky="nsew")
        self.update_button.grid(row=5, column=1, sticky="nsew")

    def refresh(self):
        # Restaurer la fenêtre avec la valeur du membre et annuler l'édition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self.M_NumSerie_entry.delete(0, END)
        self.M_NumSerie_entry.insert(0, self._Moteur['M_NumSerie'])
        self.M_NumSerie_entry.config(state=DISABLED)
        self.M_Modele_entry.delete(0, END)
        self.M_Modele_entry.insert(0, self._Moteur['M_Modele'])
        self.M_Modele_entry.config(state=DISABLED)
        self.edit_button.grid(row=5, column=1, sticky="nsew")
        self.remove_button.grid(row=5, column=2, sticky="nsew")

    def update(self):

        data = dict(M_NumSerie=self.M_NumSerie_entry.get(), M_Modele=self.M_Modele_entry.get())
        Moteur = self._Moteur_controller.update_Moteur(self._Moteur['id'], data)
        self._Moteur = Moteur
        self.refresh()

    def remove(self):
        Moteur_id = self._Moteur['id']
        self._Moteur_controller.delete_Moteur(Moteur_id)
        # afficher la confirmation
        messagebox.showinfo("Success",
                            "Moteur %s %s deleted !" % (self._Moteur['M_NumSerie'], self._Moteur['M_Modele']))
        self.back()
