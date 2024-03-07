# security/user_verification.py

from models import User
from database.db_connector import Session

# Función para verificar si un usuario está registrado
def is_user_registered(telegram_id: int) -> bool:
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    session.close()
    return user is not None

# Función para verificar si un usuario tiene un rol específico
def is_user_with_role(telegram_id: int, role: str) -> bool:
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id, role=role).first()
    session.close()
    return user is not None
