

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from controller.Bras_controller import BrasController as B
from controller.Moteur_controller import MoteurController as M

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionMicrocontroleurFrame(BaseFrame):

    def __init__(self, Microcontroleur_controller, Bras_controller,Moteur_controller,  master=None):
        super().__init__(master)
        self._Microcontroleur_controller = Microcontroleur_controller
        self._Bras_controller = Bras_controller
        self._Moteur_controller = Moteur_controller
        self._Brass= None
        self._Bras = None
        self._Moteurs = None
        self._Moteur = None
        self.create_widgets()

    def create_widgets(self):

        self.MC_NumSerie_entry = self.create_entry("MC_NumSerie", row=0)
        self.MC_Modele_entry = self.create_entry("MC_Modele", row=1)
        self.MC_Etat_entry = self.create_entry("MC_Etat", text='S', row=2, disabled=True, columnspan=3)
        NON = Label(self,text="M_ID")
        NON.grid(row=3)
        self._Moteurs = self._Moteur_controller.list_Moteur()
        listrandom1=[]
        for index, moteurs in enumerate(self._Moteurs):
            text = moteurs['M_NumSerie']
            listrandom1.insert(index, text)
        self.M_ID_entry = ttk.Combobox(self,value=listrandom1)
        self.M_ID_entry.grid(row=3,column=1)
        OUI = Label(self,text="B_ID")
        OUI.grid(row=4)
        self._Brass = self._Bras_controller.list_Bras()
        listrandom=[]
        for index, bras in enumerate(self._Brass):
            text = bras['B_NumSerie']
            listrandom.insert(index, text)
        self.B_ID_entry = ttk.Combobox(self,value=listrandom)
        self.B_ID_entry.grid(row=4,column=1)



        self.valid = Button(self, text="Valider", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="Annuler", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=5, column=1, sticky=E)
        self.cancel.grid(row=5, column=2, sticky=W)

    def valid(self):
        self._Moteur = self._Moteur_controller.search_Moteur(self.M_ID_entry.get())
        self._Bras = self._Bras_controller.search_Bras(self.B_ID_entry.get())

        data = dict(MC_NumSerie=self.MC_NumSerie_entry.get(), MC_Modele=self.MC_Modele_entry.get(), MC_Etat=self.MC_Etat_entry.get(), M_ID=self._Moteur['id'], B_ID=self._Bras['id'])
        try:
            Microcontroleur_data = self._Microcontroleur_controller.create_Microcontroleur(data)
            messagebox.showinfo("Success",
                                "Microcontroleur %s %s created !" % (Microcontroleur_data['MC_NumSerie'], Microcontroleur_data['MC_Modele']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
