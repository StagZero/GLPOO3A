import re

from model.dao.Bras_dao import BrasDAO
from exceptions import Error, InvalidData


class BrasController:
    """
    Bras actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_Bras(self):


        with self._database_engine.new_session() as session:
            Brass = BrasDAO(session).get_all()
            Brass_data = [Bras.to_dict() for Bras in Brass]

        session.commit()
        session.close()
        return Brass_data

    def get_Bras(self, Bras_id):
        with self._database_engine.new_session() as session:
            Bras = BrasDAO(session).get(Bras_id)
            Bras_data = Bras.to_dict()
        return Bras_data

    def create_Bras(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save Bras in database
                Bras = BrasDAO(session).create(data)
                Bras_data = Bras.to_dict()
                return Bras_data
        except Error as e:
            #  log error
            raise e
    def update_Bras(self, Bras_id, Bras_data):
        with self._database_engine.new_session() as session:
            Bras_dao = BrasDAO(session)
            Bras = Bras_dao.get(Bras_id)
            Bras = Bras_dao.update(Bras, Bras_data)
            return Bras.to_dict()

    def delete_Bras(self, Bras_id):

        with self._database_engine.new_session() as session:
            Bras_dao = BrasDAO(session)
            Bras = Bras_dao.get(Bras_id)
            Bras_dao.delete(Bras)
    def search_Bras(self, B_NumSerie):

        # Query database
        with self._database_engine.new_session() as session:
            Bras_dao = BrasDAO(session)
            Bras = Bras_dao.get_by_NumSerie(B_NumSerie)
            return Bras.to_dict()
