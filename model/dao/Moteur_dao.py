from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.Moteur import Moteur
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class MoteurDAO(DAO):
    """
    Moteur Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Moteur).filter_by(id=id).order_by(Moteur.M_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Moteur).order_by(Moteur.M_NumSerie).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_NumSerie(self, M_NumSerie: str):
        try:
            return self._database_session.query(Moteur).filter_by(M_NumSerie=M_NumSerie).order_by(Moteur.M_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            moteur = Moteur(M_NumSerie=data['M_NumSerie'],M_Modele=data['M_Modele'])
            self._database_session.add(moteur)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Ce Moteur est Déjà dans la Base")
        return moteur

    def update(self, Moteur: Moteur, data: dict):
        if 'M_NumSerie' in data:
            Moteur.M_NumSerie = data['M_NumSerie']
        if 'M_Modele' in data:
            Moteur.M_Modele = data['M_Modele']
        try:
            self._database_session.merge(Moteur)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur data peut etre mal formé")
        return Moteur

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
