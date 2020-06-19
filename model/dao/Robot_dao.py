from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.Robot import Robot
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound


class RobotDAO(DAO):
    """
    Robot Mapping DAO
    """
    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Robot).filter_by(id=id).order_by(Robot.R_Nom).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Robot).order_by(Robot.R_Nom).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_Nom(self, R_Nom: str):
        try:
            return self._database_session.query(Robot).filter_by(R_Nom=R_Nom).order_by(Robot.R_Nom).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_Microcontroleur(self, MC_ID: str):
        try:
            return self.__data_session.query(Robot).filter_by(MC_ID=Mc_ID).order_by(Robot.R_Nom).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            robot = Robot(MC_ID=data['MC_ID'],R_Nom=data['R_Nom'])
            self._database_session.add(robot)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Ce Robot est Déjà dans la Base")
        return robot

    def update(self, Robot: Robot, data: dict):
        if 'R_Nom' in data:
            Robot.R_Nom = data['R_Nom']
        if 'MC_ID' in data:
            Robot.MC_ID = data['MC_ID']
        try:
            self._database_session.merge(Robot)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Erreur data peut etre mal formé")
        return Robot

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
