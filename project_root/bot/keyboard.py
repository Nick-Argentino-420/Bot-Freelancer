# keyboard.py

from telegram import ReplyKeyboardMarkup, KeyboardButton

# Función para crear un teclado personalizado
def create_keyboard(buttons: list) -> ReplyKeyboardMarkup:
    keyboard = [buttons[i:i + 2] for i in range(0, len(buttons), 2)]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Botones de registro
register_buttons = [KeyboardButton("Trabajador"), KeyboardButton("Cliente")]
register_keyboard = create_keyboard(register_buttons)

# Botones adicionales para manejo de subastas
auction_buttons = [KeyboardButton("/createauction"), KeyboardButton("/bid")]
auction_keyboard = create_keyboard(auction_buttons)

# Botones adicionales para selección de ganador y pago
winner_payment_buttons = [KeyboardButton("/selectwinner"), KeyboardButton("/paymentanddelivery")]
winner_payment_keyboard = create_keyboard(winner_payment_buttons)
