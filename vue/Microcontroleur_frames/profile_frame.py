from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class ProfileMicrocontroleurFrame(BaseFrame):

    def __init__(self, Microcontroleur_controller, Microcontroleur, master=None):
        super().__init__(master)
        self._Microcontroleur = Microcontroleur
        self._Microcontroleur_controller = Microcontroleur_controller
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="Profile: ")
        self.title.grid(row=0, column=0, sticky=W)

        self.MC_NumSerie_entry = self.create_entry("MC_NumSerie: ", text=self._Microcontroleur['MC_NumSerie'],
                                                  row=1,disabled=True, columnspan=3)
        self.MC_Modele_entry = self.create_entry("MC_Modele: ", text=self._Microcontroleur['MC_Modele'],
                                                row=2, disabled=True, columnspan=3)
        self.MC_Etat_entry = self.create_entry("MC_Etat: ", text=self._Microcontroleur['MC_Etat'],
                                                row=3, disabled=True, columnspan=3)
        self.M_ID_entry = self.create_entry("M_ID: ", text=self._Microcontroleur['M_ID'],
                                                row=4, disabled=True, columnspan=3)
        self.B_ID_entry = self.create_entry("B_ID: ", text=self._Microcontroleur['B_ID'],
                                                row=5, disabled=True, columnspan=3)


        #Boutons
        self.edit_button = Button(self, text="Editer", command=self.edit)
        self.cancel_button = Button(self, text="Annuler", command=self.refresh)
        self.update_button = Button(self, text="Modifier", command=self.update)
        self.remove_button = Button(self, text="Supprimer", command=self.remove)
        self.return_button = Button(self, text="Retour", fg="red", command=self.back)
        self.return_button.grid(row=6,column=0)
        self.edit_button.grid(row=6,column=1, sticky="nsew")
        self.remove_button.grid(row=6,column=2, sticky="nsew")

    def edit(self):
        self.edit_button.grid_forget()
        self.remove_button.grid_forget()
        self.MC_NumSerie_entry.config(state=NORMAL)
        self.MC_Modele_entry.config(state=NORMAL)
        self.MC_Etat_entry.config(state=NORMAL)
        self.M_ID_entry.config(state=NORMAL)
        self.B_ID_entry.config(state=NORMAL)
        self.cancel_button.grid(row=6, column=2, sticky="nsew")
        self.update_button.grid(row=6, column=1, sticky="nsew")

    def refresh(self):
        # Restaurer la fenêtre avec la valeur du membre et annuler l'édition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self.MC_NumSerie_entry.delete(0, END)
        self.MC_NumSerie_entry.insert(0, self._Microcontroleur['MC_NumSerie'])
        self.MC_NumSerie_entry.config(state=DISABLED)
        self.MC_Modele_entry.delete(0, END)
        self.MC_Modele_entry.insert(0, self._Microcontroleur['MC_Modele'])
        self.MC_Modele_entry.config(state=DISABLED)
        self.MC_Etat_entry.delete(0, END)
        self.MC_Etat_entry.insert(0, self._Microcontroleur['MC_Etat'])
        self.MC_Etat_entry.config(state=DISABLED)
        self.M_ID_entry.delete(0, END)
        self.M_ID_entry.insert(0, self._Microcontroleur['M_ID'])
        self.M_ID_entry.config(state=DISABLED)
        self.B_ID_entry.delete(0, END)
        self.B_ID_entry.insert(0, self._Microcontroleur['B_ID'])
        self.B_ID_entry.config(state=DISABLED)
        self.edit_button.grid(row=6, column=1, sticky="nsew")
        self.remove_button.grid(row=6, column=2, sticky="nsew")

    def update(self):

        data = dict(MC_NumSerie=self.MC_NumSerie_entry.get(), MC_Modele=self.MC_Modele_entry.get(), MC_Etat=self.MC_Etat_entry.get(), M_ID=self.M_ID_entry.get(), B_ID=self.B_ID_entry.get())
        Microcontroleur = self._Microcontroleur_controller.update_Microcontroleur(self._Microcontroleur['id'], data)
        self._Microcontroleur = Microcontroleur
        self.refresh()

    def remove(self):
        Microcontroleur_id = self._Microcontroleur['id']
        self._Microcontroleur_controller.delete_Microcontroleur(Microcontroleur_id)
        # afficher la confirmation
        messagebox.showinfo("Success",
                            "Microcontroleur %s %s deleted !" % (self._Microcontroleur['MC_NumSerie'], self._Microcontroleur['MC_Modele']))
        self.back()
