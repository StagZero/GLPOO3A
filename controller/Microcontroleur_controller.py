import re

from model.dao.Microcontroleur_dao import MicrocontroleurDAO
from exceptions import Error, InvalidData


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
