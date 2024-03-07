# migrations/001_initial_migration.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from alembic import op
import sqlalchemy as sa

# Configuración de la conexión a la base de datos MySQL
DATABASE_URL = "mysql://usuario:contraseña@localhost/nombre_base_de_datos"  # Reemplazar con la información de tu base de datos
engine = create_engine(DATABASE_URL)

# Creación de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de datos declarativa para las migraciones
Base = declarative_base()

# Modelo de usuario para la migración
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, index=True)
    role = Column(String(20), default="Unregistered")
    skills = Column(String(255), nullable=True)
    experiences = Column(String(255), nullable=True)
    hourly_rate = Column(Integer, nullable=True)
    contact_info = Column(String(255), nullable=True)
    payment_method = Column(String(50), nullable=True)

# Modelo de subasta para la migración
class Auction(Base):
    __tablename__ = "auctions"
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, index=True)
    description = Column(String(255))
    duration = Column(Integer)
    start_price = Column(Integer)
    max_price = Column(Integer)
    created_at = Column(Integer)

# Creación de las tablas en la base de datos
def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.Integer(), nullable=True),
        sa.Column("role", sa.String(length=20), nullable=True),
        sa.Column("skills", sa.String(length=255), nullable=True),
        sa.Column("experiences", sa.String(length=255), nullable=True),
        sa.Column("hourly_rate", sa.Integer(), nullable=True),
        sa.Column("contact_info", sa.String(length=255), nullable=True),
        sa.Column("payment_method", sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )

    op.create_table(
        "auctions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("client_id", sa.Integer(), nullable=True),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("duration", sa.Integer(), nullable=True),
        sa.Column("start_price", sa.Integer(), nullable=True),
        sa.Column("max_price", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
