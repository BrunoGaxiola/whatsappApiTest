import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Import environment variables.
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
API_URL = os.getenv("WHATSAPP_API_URL")
TO_PHONE_NUMBER = os.getenv("RECEIVER_PHONE_NUMBER")

# Function to send a message.
def sendMessage():
    url = f"{API_URL}/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",    
        "recipient_type": "individual",
        "to": TO_PHONE_NUMBER,
        "type": "template",
        "template": {
            "name": "cita_taller_buena",
            "language": {"code": "es_MX"},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "parameter_name": "nombre",
                            "text": "Fredi Gaxiola Gutierrez"
                        },
                        {
                            "type": "text",
                            "parameter_name": "nom_suc",
                            "text": "Econollantas Quiroga"
                        },
                        {
                            "type": "text",
                            "parameter_name": "fecha",
                            "text": "jueves 15 de enero"
                        },
                        {
                            "type": "text",
                            "parameter_name": "hora",
                            "text": "13:00"
                        }
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("✅ Message sent successfully!")
        print(response.json())
        #print(response.)
    else:
        print("❌ Failed to send message:")
        print(response.status_code, response.text)

# Main program.
if __name__ == "__main__":
    sendMessage()