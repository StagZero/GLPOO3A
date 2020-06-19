from model.database import DatabaseEngine
from controller.Bras_controller import BrasController
from controller.Moteur_controller import MoteurController
from controller.Microcontroleur_controller import MicrocontroleurController
from controller.Robot_controller import RobotController

from vue.root_frame import RootFrame


def main():
    print("Bienvenue dans le Createur de Robot")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///Robot.db')
    database_engine.create_database()

    # controller
    Bras_controller = BrasController(database_engine)
    Moteur_controller = MoteurController(database_engine)
    Microcontroleur_controller = MicrocontroleurController(database_engine)
    Robot_controller = RobotController(database_engine)
    

    # init vue
    root = RootFrame(Bras_controller, Moteur_controller, Microcontroleur_controller,Robot_controller)
    root.master.title("Creation Robot")
    root.show_menu()

    # start
    root.mainloop()


if __name__ == "__main__":
    main()
