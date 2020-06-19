import re
import time

from tkinter import messagebox
from model.dao.Microcontroleur_dao import MicrocontroleurDAO
from exceptions import Error, InvalidData
from controller.Bras_controller import BrasController as B
from controller.Moteur_controller import MoteurController as M

class MicrocontroleurController:
    """
    Microcontroleur actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_Microcontroleur(self):


        with self._database_engine.new_session() as session:
            Microcontroleurs = MicrocontroleurDAO(session).get_all()
            Microcontroleurs_data = [Microcontroleur.to_dict() for Microcontroleur in Microcontroleurs]

        session.commit()
        session.close()
        return Microcontroleurs_data

    def get_Microcontroleur(self, Microcontroleur_id):
        with self._database_engine.new_session() as session:
            Microcontroleur = MicrocontroleurDAO(session).get(Microcontroleur_id)
            Microcontroleur_data = Microcontroleur.to_dict()
        return Microcontroleur_data

    def create_Microcontroleur(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save Microcontroleur in database
                Microcontroleur = MicrocontroleurDAO(session).create(data)
                Microcontroleur_data = Microcontroleur.to_dict()
                return Microcontroleur_data
        except Error as e:
            #  log error
            raise e
    def update_Microcontroleur(self, Microcontroleur_id, Microcontroleur_data):
        with self._database_engine.new_session() as session:
            Microcontroleur_dao = MicrocontroleurDAO(session)
            Microcontroleur = Microcontroleur_dao.get(Microcontroleur_id)
            Microcontroleur = Microcontroleur_dao.update(Microcontroleur, Microcontroleur_data)
            return Microcontroleur.to_dict()

    def delete_Microcontroleur(self, Microcontroleur_id):

        with self._database_engine.new_session() as session:
            Microcontroleur_dao = MicrocontroleurDAO(session)
            Microcontroleur = Microcontroleur_dao.get(Microcontroleur_id)
            Microcontroleur_dao.delete(Microcontroleur)
    def search_Microcontroleur(self, MC_NumSerie):

        # Query database
        with self._database_engine.new_session() as session:
            Microcontroleur_dao = MicrocontroleurDAO(session)
            Microcontroleur = Microcontroleur_dao.get_by_NumSerie(MC_NumSerie)
            return Microcontroleur.to_dict()



    def get_Etat(self, MC_id):
        with self._database_engine.new_session() as session:
           Microcontroleur = MicrocontroleurDAO(session).get(MC_id)
        return Microcontroleur['MC_Etat']

    def attendre_3s(self):

        time.sleep(3)

    def attendre_30s(self):
        #nous avons mis 10s pour des raisons de practicité lors des tests
        time.sleep(10)

    def start(self, MC_ID):

        MC = self.get_Microcontroleur(MC_ID)
        BrasC = B(self._database_engine)
        MoteurC = M(self._database_engine)
        B.serrer(BrasC, MC['B_ID'])
        
        data1 = dict(MC_Etat="A")
        self.update_Microcontroleur(MC_ID, data1)
        MC = self.get_Microcontroleur(MC_ID)
        messagebox.showinfo("Success",
                            "Le robot est dans l'état %s" % MC['MC_Etat'])
        self.attendre_3s()
        M.droite(MoteurC,MC['M_ID'])

        data2 = dict(MC_Etat="AB")
        self.update_Microcontroleur(MC_ID, data2)
        MC = self.get_Microcontroleur(MC_ID)
        messagebox.showinfo("Success",
                            "Le robot est dans l'état %s" % MC['MC_Etat'])
        
        self.attendre_30s()
        M.arreter(MoteurC,MC['M_ID'])
        B.lacher(BrasC,MC['B_ID'])

        data3 = dict(MC_Etat="B")
        self.update_Microcontroleur(MC_ID, data3)
        MC = self.get_Microcontroleur(MC_ID)
        messagebox.showinfo("Success",
                            "Le robot est dans l'état %s" % MC['MC_Etat'])
        
        self.attendre_3s()
        M.gauche(MoteurC,MC['M_ID'])

        data4 = dict(MC_Etat="BS")
        self.update_Microcontroleur(MC_ID, data4)
        MC = self.get_Microcontroleur(MC_ID)
        messagebox.showinfo("Success",
                            "Le robot est dans l'état %s" % MC['MC_Etat'])
        
        self.attendre_30s()
        M.arreter(MoteurC,MC['M_ID'])

        data5 = dict(MC_Etat="S")
        self.update_Microcontroleur(MC_ID, data5)
        MC = self.get_Microcontroleur(MC_ID)
        messagebox.showinfo("Success",
                            "Le robot est dans l'état %s" % MC['MC_Etat'])