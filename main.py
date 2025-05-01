from flask import Flask, request
import telebot

TOKEN = "7912943320:AAE0SSzTo23l7XzQuhmDEWHOhjtWG-fcCOQ"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://valuesniperbot.onrender.com/' + TOKEN)
    return 'Webhook connecté !', 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur StatistiquesbetBot ! Envoie deux équipes pour commencer l’analyse.")

@bot.message_handler(func=lambda message: True)
def analyse_match(message):
    bot.reply_to(message, f"Analyse en cours pour le match : {message.text} ... (fonctionnalité à venir)")