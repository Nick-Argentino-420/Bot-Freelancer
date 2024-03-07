# handlers.py

from telegram import Update
from telegram.ext import CallbackContext
from models import User, Auction
from utils import get_user_role, create_keyboard, get_auction_details

# Controlador para el comando /start
def start_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Unregistered":
        update.message.reply_text("¡Bienvenido! Por favor, regístrate usando /register como Trabajador o Cliente.")
    else:
        update.message.reply_text(f"Bienvenido de nuevo, {user_role}.")

# Controlador para el comando /help
def help_handler(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Este bot te permite realizar subastas y pujar por trabajos. "
                              "Puedes usar los siguientes comandos:\n"
                              "/register - Regístrate como Trabajador o Cliente\n"
                              "/createauction - Crea una subasta\n"
                              "/bid - Puja por una subasta\n"
                              "/selectwinner - Selecciona al ganador de una subasta\n"
                              "/paymentanddelivery - Realiza el pago y la entrega del trabajo")

# Controlador para el comando /register
def register_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Unregistered":
        update.message.reply_text("¡Registro exitoso! Ahora, completa tu perfil.")
        update.message.reply_text("Por favor, ingresa tus habilidades, experiencias y precio por hora (si eres Trabajador), "
                                  "o tu información de contacto y método de pago (si eres Cliente).")
        # Lógica adicional para procesar el registro

    else:
        update.message.reply_text("Ya estás registrado como Trabajador o Cliente.")

# Controlador para el comando /createauction
def create_auction_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Cliente":
        update.message.reply_text("Excelente, creemos una subasta. Por favor, proporciona los detalles de la subasta, "
                                  "la duración, el precio inicial y/o máximo.")
        # Lógica adicional para procesar la creación de subasta

    else:
        update.message.reply_text("Solo los Clientes pueden crear subastas. Si eres Trabajador, puedes pujar por subastas "
                                  "usando el comando /bid.")

# Controlador para el comando /bid
def bid_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Trabajador":
        update.message.reply_text("Perfecto, veamos las subastas disponibles y puja por la que te interese.")
        # Lógica adicional para procesar la puja por la subasta

    else:
        update.message.reply_text("Solo los Trabajadores pueden pujar por subastas. Si eres Cliente, puedes crear "
                                  "subastas usando el comando /createauction.")

# Controlador para el comando /selectwinner
def select_winner_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Cliente":
        update.message.reply_text("Es hora de seleccionar al ganador de tu subasta. Revisa las pujas y elige al Trabajador "
                                  "que realizará el trabajo.")
        # Lógica adicional para procesar la selección del ganador

    else:
        update.message.reply_text("Solo los Clientes pueden seleccionar al ganador de una subasta. Si eres Trabajador, "
                                  "puedes esperar a ser elegido o participar en otras subastas.")

# Controlador para el comando /paymentanddelivery
def payment_and_delivery_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_role = get_user_role(user_id)

    if user_role == "Cliente":
        update.message.reply_text("Perfecto, una vez que el Trabajador entregue el trabajo, puedes realizar el pago y "
                                  "aprobar la entrega usando este comando.")
        # Lógica adicional para procesar el pago y la entrega

    else:
        update.message.reply_text("Solo los Clientes pueden realizar el pago y aprobar la entrega. Si eres Trabajador, "
                                  "debes esperar a que el Cliente realice estas acciones.")
