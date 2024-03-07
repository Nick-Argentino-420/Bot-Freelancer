# bot/main.py

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from handlers import start_handler, help_handler, register_handler, create_auction_handler, \
    bid_handler, select_winner_handler, payment_and_delivery_handler, unknown_handler
from config import Config
from database.db_connector import run_migrations

# Configuración del registro de logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Función principal que maneja los comandos y mensajes
def main() -> None:
    # Inicialización del bot
    updater = Updater(Config.TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Configuración de los controladores de comandos
    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("help", help_handler))
    dispatcher.add_handler(CommandHandler("register", register_handler))
    dispatcher.add_handler(CommandHandler("createauction", create_auction_handler))
    dispatcher.add_handler(CommandHandler("bid", bid_handler))
    dispatcher.add_handler(CommandHandler("selectwinner", select_winner_handler))
    dispatcher.add_handler(CommandHandler("paymentanddelivery", payment_and_delivery_handler))

    # Manejo de mensajes no reconocidos
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown_handler))

    # Inicio del bot
    try:
        updater.start_polling()
        logger.info("Bot iniciado. Presiona Ctrl+C para detenerlo.")
        updater.idle()
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")

# Punto de entrada del programa

if __name__ == '__main__':
    # Realizar migraciones al iniciar el bot por primera vez
    run_migrations()

    # Iniciar el bot
    main()
