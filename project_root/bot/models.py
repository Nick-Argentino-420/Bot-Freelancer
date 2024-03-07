# models.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definición de la base de datos y sesión
Base = declarative_base()
engine = create_engine("mysql://usuario:contraseña@localhost/nombre_base_de_datos")  # Reemplazar con la información de tu base de datos
Session = sessionmaker(bind=engine)

# Modelo de usuario
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    role = Column(String(20), default="Unregistered")  # Puede ser "Trabajador", "Cliente", o "Unregistered"
    skills = Column(String(255), nullable=True)
    experiences = Column(String(255), nullable=True)
    hourly_rate = Column(Integer, nullable=True)
    contact_info = Column(String(255), nullable=True)
    payment_method = Column(String(50), nullable=True)

# Modelo de subasta
class Auction(Base):
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, index=True)
    description = Column(String(255))
    duration = Column(Integer)
    start_price = Column(Integer)
    max_price = Column(Integer)
    created_at = Column(Integer)  # Puede ser útil para ordenar y filtrar subastas por fecha de creación

    # Métodos adicionales según sea necesario para manipular y obtener detalles de la subasta
    def get_auction_details(self):
        return f"Descripción: {self.description}\n" \
               f"Duración: {self.duration} horas\n" \
               f"Precio Inicial: {self.start_price}\n" \
               f"Precio Máximo: {self.max_price}"

    # Otros métodos según sea necesario para la manipulación de datos de la subasta
