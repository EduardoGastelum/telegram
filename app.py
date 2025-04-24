from flask import Flask, request
from dotenv import load_dotenv
import os
import telegram

# Carga variables de .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY      = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text    = update.message.text

    # Respuesta simple de prueba
    bot.send_message(chat_id=chat_id, text=f"Recibí tu mensaje: {text}")
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)