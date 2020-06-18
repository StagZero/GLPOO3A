from model.database import DatabaseEngine
from controller.Bras_controller import BrasController

def main():
    print("Bienvenue dans le Createur de Robot")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///Robot.db')
    database_engine.create_database()

    # controller
    Bras_controller = BrasController(database_engine)

if __name__ == "__main__":
    main()
