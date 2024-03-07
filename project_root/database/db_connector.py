# db_connector.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import command
from alembic.config import Config as AlembicConfig
from config import Config  # Importar la configuración del proyecto

# Configuración de la conexión a la base de datos MySQL
DATABASE_URL = Config.DATABASE_URL
engine = create_engine(DATABASE_URL)

# Creación de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para realizar la migración
def run_migrations():
    alembic_cfg = AlembicConfig("alembic.ini")  # Asegúrate de tener el archivo alembic.ini configurado correctamente
    command.upgrade(alembic_cfg, "head")
