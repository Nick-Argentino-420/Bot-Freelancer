# messaging/notifications.py

from telegram import Bot
from models import User
from database.db_connector import Session

# Función para enviar una notificación a un usuario
def send_notification(telegram_id: int, message: str) -> None:
    bot = Bot(token="TELEGRAM_BOT_TOKEN")  # Reemplazar con el token real de tu bot
    bot.send_message(chat_id=telegram_id, text=message)

# Función para enviar una notificación a todos los trabajadores
def send_notification_to_workers(message: str) -> None:
    session = Session()
    workers = session.query(User).filter_by(role="Trabajador").all()
    session.close()

    for worker in workers:
        send_notification(worker.telegram_id, message)
