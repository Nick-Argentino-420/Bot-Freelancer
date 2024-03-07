# monetization/commissions.py

from models import Auction
from database.db_connector import Session

# Función para calcular la comisión por una subasta
def calculate_commission(auction_id: int) -> float:
    session = Session()
    auction = session.query(Auction).filter_by(id=auction_id).first()
    session.close()

    if auction:
        # Lógica para calcular la comisión según el precio final o algún otro criterio
        # Puedes definir tus propias reglas de comisión y ajustar esta función en consecuencia
        return auction.final_price * 0.1  # Ejemplo: comisión del 10% sobre el precio final
    else:
        return 0.0
