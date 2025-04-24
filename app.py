from flask import Flask, request
import logging
from dotenv import load_dotenv
import os
import telegram

# Carga variables de .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_KEY      = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
# Enable debug logging
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)
bot = telegram.Bot(token=TELEGRAM_TOKEN)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        text    = update.message.text

        # Respuesta simple de prueba
        bot.send_message(chat_id=chat_id, text=f"Recibí tu mensaje: {text}")
        return "OK"
    except Exception as e:
        app.logger.error("Error en /webhook: %s", e, exc_info=True)
        return "Error interno", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)