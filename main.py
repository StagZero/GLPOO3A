from model.database import DatabaseEngine

def main():
    # Init db
    database_engine = DatabaseEngine(url='sqlite:///Robot.db')
    database_engine.create_database()

if __name__ == "__main__":
    main()
