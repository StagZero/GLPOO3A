from model.database import DatabaseEngine
from controller.Bras_controller import BrasController
from controller.Moteur_controller import MoteurController
from controller.Microcontroleur_controller import MicrocontroleurController

def main():
    print("Bienvenue dans le Createur de Robot")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///Robot.db')
    database_engine.create_database()

    # controller
    Bras_controller = BrasController(database_engine)
    Moteur_controller = MoteurController(database_engine)
    Microcontroleur_controller = MicrocontroleurController(database_engine)
   
    # start
    root.mainloop()


if __name__ == "__main__":
    main()
