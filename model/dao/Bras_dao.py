from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.Bras import Bras
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class BrasDAO(DAO):
    """
    Bras Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Bras).filter_by(id=id).order_by(Bras.B_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Bras).order_by(Bras.B_NumSerie).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_NumSerie(self, B_NumSerie: str):
        try:
            return self._database_session.query(Bras).filter_by(B_NumSerie=B_NumSerie).order_by(Bras.B_NumSerie).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            bras = Bras(B_NumSerie=data['B_NumSerie'],B_Modele=data['B_Modele'])
            self._database_session.add(bras)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Ce Bras est Déjà dans la Base")
        return bras

    def update(self, Bras: Bras, data: dict):
        if 'B_NumSerie' in data:
            Bras.B_NumSerie = data['B_NumSerie']
        if 'B_Modele' in data:
            Bras.B_Modele = data['B_Modele']
        try:
            self._database_session.merge(Bras)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur data peut etre mal formé")
        return Bras

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
