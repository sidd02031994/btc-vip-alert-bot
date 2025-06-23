from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    print("🚀 Webhook triggered")
    print("Incoming data:", data)

    message = data.get("message", "🚨 Alert Triggered (No message content)")

    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    r = requests.post(telegram_url, data=payload)

    print(f"Telegram API Status: {r.status_code}")
    print(f"Telegram Response: {r.text}")

    return {"ok": True, "telegram_status": r.status_code}

@app.route("/", methods=["GET"])
def health():
    return "Bot is Live", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

