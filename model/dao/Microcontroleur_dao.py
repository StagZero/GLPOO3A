from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.member import Member
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class MicrocontroleurDAO(DAO):
    """
    Microcontroleur Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self.__data_session.query(Microcontroleur).filter_by(id=id).order_by(Microcontroleur.MC_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Microcontroleur).order_by(Microcontroleur.MC_NumSerie).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_NumSerie(self, MC_NumSerie: str):
        try:
            return self._database_session.query(Microcontroleur).filter_by(MC_NumSerie=MC_NumSerie).order_by(Microcontroleur.MC_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_Bras(self, B_ID: str):
        try:
            return self._database_session.query(Microcontroleur).filter_by(B_ID=B_ID).order_by(Microcontroleur.MC_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_Moteur(self, M_ID: str):
        try:
            return self._database_session.query(Microcontroleur).filter_by(M_ID=M_ID).order_by(Microcontroleur.MC_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()


    def create(self, data: dict):
        try:
            Microcontroleur = Microcontroleur(B_ID=data.get('B_ID'), M_ID=data.get('M_ID'),MC_NumSerie=data.get('MC_NumSerie'),MC_Modele=data.get('MC_Modele'),M_Etat=data.get('M_Etat'))
            self._database_session.add(Microcontroleur)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Ce µcontroleur est Déjà dans la Base")
        return Microcontroleur

    def update(self, Microcontroleur: Microcontroleur, data: dict):
        if 'MC_NumSerie' in data:
            Microcontroleur.MC_NumSerie = data['MC_NumSerie']
        if 'MC_Modele' in data:
            Microcontroleur.MC_Modele = data['MC_Modele']
        if 'MC_Etat' in data:
            Microcontroleur.MC_Etat = data['MC_Etat']
        if 'B_ID' in data:
            Microcontroleur.B_ID = data['B_ID']
        if 'M_ID' in data:
            Microcontroleur.M_ID = data['M_ID   ']
        try:
            self._database_session.merge(Microcontroleur)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur data peut etre mal formé")
        return Microcontroleur

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
