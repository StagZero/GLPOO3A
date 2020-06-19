import re
from tkinter import messagebox
from model.dao.Moteur_dao import MoteurDAO
from exceptions import Error, InvalidData


class MoteurController:
    """
    Moteur actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_Moteur(self):


        with self._database_engine.new_session() as session:
            Moteurs = MoteurDAO(session).get_all()
            Moteurs_data = [Moteur.to_dict() for Moteur in Moteurs]

        session.commit()
        session.close()
        return Moteurs_data

    def get_Moteur(self, Moteur_id):
        with self._database_engine.new_session() as session:
            Moteur = MoteurDAO(session).get(Moteur_id)
            Moteur_data = Moteur.to_dict()
        return Moteur_data

    def create_Moteur(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save Moteur in database
                Moteur = MoteurDAO(session).create(data)
                Moteur_data = Moteur.to_dict()
                return Moteur_data
        except Error as e:
            #  log error
            raise e
    def update_Moteur(self, Moteur_id, Moteur_data):
        with self._database_engine.new_session() as session:
            Moteur_dao = MoteurDAO(session)
            Moteur = Moteur_dao.get(Moteur_id)
            Moteur = Moteur_dao.update(Moteur, Moteur_data)
            return Moteur.to_dict()

    def delete_Moteur(self, Moteur_id):

        with self._database_engine.new_session() as session:
            Moteur_dao = MoteurDAO(session)
            Moteur = Moteur_dao.get(Moteur_id)
            Moteur_dao.delete(Moteur)
    def search_Moteur(self, M_NumSerie):

        # Query database
        with self._database_engine.new_session() as session:
            Moteur_dao = MoteurDAO(session)
            Moteur = Moteur_dao.get_by_NumSerie(M_NumSerie)
            return Moteur.to_dict()

    def droite(self, M_id):
        Moteur = self.get_Moteur(M_id)
        messagebox.showinfo("Success",
                            "Le moteur %s à démarré, le robot se deplace vers la droite" % Moteur['M_NumSerie'])
       
        
    def gauche(self, M_id):
        Moteur = self.get_Moteur(M_id)
        messagebox.showinfo("Success",
                            "Le moteur %s à démarré, le robot se déplace vers la gauche" % Moteur['M_NumSerie'])
        
    def arreter(self, M_id):
        Moteur = self.get_Moteur(M_id)
        messagebox.showinfo("Success",
                            "Le moteur %s s'arrete" % Moteur['M_NumSerie'])
        
        