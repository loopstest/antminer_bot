import telebot
import os

# === Ton token du BotFather (tu le mettras plus tard dans Render)
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

# ======== MENU PRINCIPAL ========
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛠 Réparation", "📰 News", "🛒 Marketplace")
    bot.send_message(message.chat.id, "👋 Bienvenue sur le bot Antminer !", reply_markup=markup)

# ======== RETOURS ========
@bot.message_handler(func=lambda msg: msg.text == "⬅️ Retour")
def retour_main(message):
    send_welcome(message)

@bot.message_handler(func=lambda msg: msg.text == "⬅️ Retour Réparation")
def retour_reparation(message):
    menu_reparation(message)

@bot.message_handler(func=lambda msg: msg.text == "⬅️ Retour modèle")
def retour_modele(message):
    menu_reparation(message)

# ======== EXEMPLE DE SOUS-MENU RÉPARATION ========
def menu_reparation(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Abnormal input voltage (S17)", "DC buck (T17)", "⬅️ Retour")
    bot.send_message(message.chat.id, "🔧 Choisis un problème de réparation :", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "🛠 Réparation")
def reparation(message):
    menu_reparation(message)

# ======== LIENS DES SOUS-MENUS ========
@bot.message_handler(func=lambda msg: "(" in msg.text and ")" in msg.text)
def lien_videos(message):
    titre = message.text.split(" (")[0].strip()
    lien = None

    liens_exemples = {
        "Abnormal input voltage": "https://t.me/ton_canal/1",
        "DC buck": "https://t.me/ton_canal/2",
        "Basic structure + power": "https://youtu.be/example1",
        "Basic signal": "https://youtu.be/example2",
    }

    if titre in liens_exemples:
        lien = liens_exemples[titre]

    if lien:
        bot.send_message(message.chat.id, f"📺 Voici la ressource pour *{titre}* :\n{lien}", parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, f"🔍 Pas encore de lien pour *{titre}*", parse_mode="Markdown")

# ======== AUTRES OPTIONS ========
@bot.message_handler(func=lambda msg: msg.text == "📰 News")
def news(message):
    bot.send_message(message.chat.id, "📰 Les dernières nouvelles Antminer seront bientôt disponibles ici.")

@bot.message_handler(func=lambda msg: msg.text == "🛒 Marketplace")
def marketplace(message):
    bot.send_message(message.chat.id, "🛒 La marketplace ASIC sera bientôt disponible.")

# ======== LANCEMENT DU BOT ========
print("✅ Bot en marche...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
bot.py