import re

from model.dao.Robot_dao import RobotDAO
from exceptions import Error, InvalidData
from controller.Microcontroleur_controller import MicrocontroleurController as MC


class RobotController:
    """
    Robot actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_Robot(self):


        with self._database_engine.new_session() as session:
            Robots = RobotDAO(session).get_all()
            Robots_data = [Robot.to_dict() for Robot in Robots]

        session.commit()
        session.close()
        return Robots_data

    def get_Robot(self, Robot_id):
        with self._database_engine.new_session() as session:
            Robot = RobotDAO(session).get(Robot_id)
            Robot_data = Robot.to_dict()
        return Robot_data

    def create_Robot(self, data):
        try:
            with self._database_engine.new_session() as session:
                # Save Robot in database
                Robot = RobotDAO(session).create(data)
                Robot_data = Robot.to_dict()
                return Robot_data
        except Error as e:
            #  log error
            raise e
    def update_Robot(self, Robot_id, Robot_data):
        with self._database_engine.new_session() as session:
            Robot_dao = RobotDAO(session)
            Robot = Robot_dao.get(Robot_id)
            Robot = Robot_dao.update(Robot, Robot_data)
            return Robot.to_dict()

    def delete_Robot(self, Robot_id):

        with self._database_engine.new_session() as session:
            Robot_dao = RobotDAO(session)
            Robot = Robot_dao.get(Robot_id)
            Robot_dao.delete(Robot)
    def search_Robot(self, R_Nom):

        # Query database
        with self._database_engine.new_session() as session:
            Robot_dao = RobotDAO(session)
            Robot = Robot_dao.get_by_Nom(R_Nom)
            return Robot.to_dict()
        
    def start(self, R_id):
        with self._database_engine.new_session() as session:
            R = self.get_Robot(R_id)
            MCC = MC(self._database_engine)
            MC.start(MCC,R['MC_ID'])
