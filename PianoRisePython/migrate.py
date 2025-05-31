from app import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Migración completada: todas las tablas han sido creadas en la base de datos.")
