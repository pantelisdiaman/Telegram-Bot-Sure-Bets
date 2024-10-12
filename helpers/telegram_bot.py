import telebot

# Create bot
bot = telebot.TeleBot(token='6817000775:AAGns9j7mMupfpQfT7_9oml2zrTGUYcCPsA')

# Send message
def sendNotification(league, match, market, matchTime, profit, bookmaker1, market1, odd1, bookmaker2, market2, odd2, bookmaker3, market3, odd3):
    message = league + "\n" + match + "\n" + matchTime + "\n\n" + market + "\n" + market1 + " - " + bookmaker1 + " - " + odd1 + "\n" + market2 + " - " + bookmaker2 + " - " + odd2 + "\n"
    
    if bookmaker3 != "":
        message = message + market3 + " - " + bookmaker3 + " - " + odd3 + "\n"
    
    message = message + "Profit: " + profit
    
    bot.send_message(-1001627502087, message)
