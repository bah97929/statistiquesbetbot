import telebot

TOKEN = "7912943320:AAE0SSzTo23l7XzQuhmDEWHOhjtWG-fcCOQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bienvenue sur le bot StatistiquesbetBot ! Envoie le nom de deux équipes pour obtenir une analyse.")

@bot.message_handler(func=lambda message: True)
def analyse_match(message):
    # Simule une réponse d'analyse (à personnaliser)
    bot.reply_to(message, f"Analyse en cours pour le match : {message.text} ... (fonctionnalité à venir)")

bot.polling()
