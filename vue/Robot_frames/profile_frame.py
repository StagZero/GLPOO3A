from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class ProfileRobotFrame(BaseFrame):

    def __init__(self, Robot_controller, Robot, Microcontroleur_controller, master=None):
        super().__init__(master)
        self._Robot = Robot
        self._Robot_controller = Robot_controller
        self._Microcontroleur_controller = Microcontroleur_controller
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="Profile: ")
        self.title.grid(row=0, column=0, sticky=W)

        self.R_Nom_entry = self.create_entry("R_Nom: ", text=self._Robot['R_Nom'],
                                                  row=1,disabled=True, columnspan=3)
        self.MC_ID_entry = self.create_entry("MC_ID: ", text=self._Robot['MC_ID'],
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
        self.R_Nom_entry.config(state=NORMAL)
        self.MC_ID_entry.config(state=NORMAL)
        self.cancel_button.grid(row=5, column=2, sticky="nsew")
        self.update_button.grid(row=5, column=1, sticky="nsew")

    def refresh(self):
        # Restaurer la fenêtre avec la valeur du membre et annuler l'édition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self.R_Nom_entry.delete(0, END)
        self.R_Nom_entry.insert(0, self._Robot['R_Nom'])
        self.R_Nom_entry.config(state=DISABLED)
        self.MC_ID_entry.delete(0, END)
        self.MC_ID_entry.insert(0, self._Robot['MC_ID'])
        self.MC_ID_entry.config(state=DISABLED)
        self.edit_button.grid(row=5, column=1, sticky="nsew")
        self.remove_button.grid(row=5, column=2, sticky="nsew")

    def update(self):

        data = dict(R_Nom=self.R_Nom_entry.get(), MC_ID=self.MC_ID_entry.get())
        Robot = self._Robot_controller.update_Robot(self._Robot['id'], data)
        self._Robot = Robot
        self.refresh()

    def remove(self):
        Robot_id = self._Robot['id']
        self._Robot_controller.delete_Robot(Robot_id)
        # afficher la confirmation
        MC = self._Microcontroleur_controller.get_Microcontroleur(self._Robot['MC_ID'])
        messagebox.showinfo("Success",
                            "Robot %s %s deleted !" % (self._Robot['R_Nom'], MC['MC_NumSerie']))
        self.back()
