# utils.py

from models import User, Auction
from database.db_connector import Session

# Función para obtener el rol de un usuario
def get_user_role(telegram_id: int) -> str:
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    session.close()
    return user.role if user else "Unregistered"

# Función para crear un teclado de selección de subastas
def create_auction_selection_keyboard() -> list:
    session = Session()
    auctions = session.query(Auction).all()
    session.close()

    buttons = [f"Subasta {auction.id}" for auction in auctions]
    return buttons

# Función para obtener detalles de una subasta
def get_auction_details(auction_id: int) -> str:
    session = Session()
    auction = session.query(Auction).filter_by(id=auction_id).first()
    session.close()

    if auction:
        details = (
            f"Descripción: {auction.description}\n"
            f"Duración: {auction.duration} horas\n"
            f"Precio Inicial: {auction.start_price}\n"
            f"Precio Máximo: {auction.max_price}"
        )
        return details
    else:
        return "Subasta no encontrada."

# Funciones adicionales según sea necesario para calcular comisiones, verificar usuarios de una puja, etc.
def calculate_commission(amount: float) -> float:
    # Lógica para calcular comisión
    # (Agregar la lógica según sea necesario)
    pass

def verify_bid_user(user_id: int, auction_id: int) -> bool:
    # Lógica para verificar al usuario de una puja
    # (Agregar la lógica según sea necesario)
    pass
