# tests/test_handlers.py

from bot.handlers import start_handler
from telegram import Update
from unittest.mock import Mock

def test_start_handler():
    update = Mock(spec=Update)
    context = Mock()

    # Ejemplo de prueba para el comando /start
    update.message.from_user.id = 123
    update.message.reply_text = Mock()
    start_handler(update, context)

    # Verificar que se llamó al método correcto con los argumentos correctos
    update.message.reply_text.assert_called_once_with("Bienvenido de nuevo, Unregistered.")