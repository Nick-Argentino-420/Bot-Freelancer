# payments/paypal.py

import requests
from config import Config  # Importar la configuración del proyecto

PAYPAL_API_URL = "https://api.paypal.com"  # Reemplazar con la URL correcta de la API de PayPal
PAYPAL_CLIENT_ID = Config.PAYPAL_CLIENT_ID
PAYPAL_SECRET = Config.PAYPAL_SECRET

def create_payment(amount: float, currency: str, description: str, redirect_url: str) -> str:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_access_token()}"
    }

    data = {
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "transactions": [{
            "amount": {
                "total": f"{amount:.2f}",
                "currency": currency
            },
            "description": description
        }],
        "redirect_urls": {
            "return_url": redirect_url,
            "cancel_url": redirect_url
        }
    }

    response = requests.post(f"{PAYPAL_API_URL}/v1/payments/payment", headers=headers, json=data)
    payment_id = response.json()["id"]

    return payment_id

def execute_payment(payment_id: str, payer_id: str) -> bool:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_access_token()}"
    }

    data = {
        "payer_id": payer_id
    }

    response = requests.post(f"{PAYPAL_API_URL}/v1/payments/payment/{payment_id}/execute", headers=headers, json=data)
    return response.json()["state"] == "approved"

def get_access_token() -> str:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    response = requests.post(f"{PAYPAL_API_URL}/v1/oauth2/token", headers=headers, data=data, auth=(PAYPAL_CLIENT_ID, PAYPAL_SECRET))
    access_token = response.json()["access_token"]

    return access_token
