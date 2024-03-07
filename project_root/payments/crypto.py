# payments/crypto.py

from binance.client import Client
from config import Config  # Importar la configuración del proyecto

BINANCE_API_KEY = Config.BINANCE_API_KEY
BINANCE_API_SECRET = Config.BINANCE_API_SECRET

def generate_crypto_address() -> dict:
    client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)
    
    # Supongamos que quieres generar una dirección de depósito para BTC
    # Puedes ajustar el símbolo según la criptomoneda deseada (BTC, ETH, SOL, etc.)
    deposit_address = client.get_deposit_address(asset='BTC')

    return deposit_address['address']

def check_crypto_payment(address: str, amount: float) -> bool:
    # Implementar la lógica para verificar el pago en la criptomoneda
    # En Binance, puedes usar la API de historial de operaciones para verificar transacciones
    client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)
    trades = client.get_my_trades(symbol='BTCUSDT', limit=5)  # Cambia el símbolo según la criptomoneda que estés utilizando

    # Verificar si hay alguna transacción con la dirección específica y el monto esperado
    for trade in trades:
        if trade['isBuyer'] and trade['address'] == address and float(trade['qty']) == amount:
            return True

    return False
