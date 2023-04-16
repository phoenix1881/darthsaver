import os

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message,
                 '''
Welcome, young Padawan, to your personal expense tracker.
I am your guide, Darth Vader.
By default, you can divide your expenses into 7 categories:

- Food and dining
- Transportation
- Housing
- Entertainment
- Wellness
- Personal care
- Miscellaneous

To add an expense, simply specify the category with the first letter (capital or small letter) followed by the amount
spent. For example, to log a ₹20 food expense, you can use the command "f 20" or "F 20".

To set your name, use the command /setName followed by your name. For example: /setName Luke Skywalker

You may also set your monthly budget for each category using the command /setBudget followed by the category name and the budget amount. Use your powers wisely, Padawan.

And should you require any assistance, do not hesitate to call upon me by typing /help. I am always watching.
''')


#
# @bot.message_handler(commands=['setName'])
# def set_name(message):
#


#
# import os
#
# import telebot
#
# from sql import get_daily_horoscope
#
# BOT_TOKEN = os.environ.get('BOT_TOKEN')
#
# bot = telebot.TeleBot(BOT_TOKEN)
#
#
# # print all messaages
#
# import logging
#
# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#
# # Log incoming messages
# def handle_message(update, context):
#     logging.info(f"Message from {update.message.chat_id}: {update.message.text}")
#
# # Log outgoing messages
# def send_message(update, context, message):
#     context.bot.send_message(chat_id=update.message.chat_id, text=message)
#     logging.info(f"Message to {update.message.chat_id}: {message}")
#
#
@bot.message_handler(commands=['setName'])
def set_Name(message):
    # bot.reply_to(message, "Howdy, how are you doing?")
    # bot.send_message(message.chat.id, "Howdy, how are you doing?")
    text = "What's your name Young Padawan?"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, name_handler())
    print(bot.register_next_step_handler(sent_msg, name_handler()))



def name_handler(message):
    name = message.text
    sent_msg = bot.send_message(message.chat.id, "Your name has been set to " + name)
    bot.register_next_step_handler(sent_msg)
#
# @bot.message_handler(commands=['horoscope'])
# def sign_handler(message):
#     text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
#     sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(sent_msg, day_handler)
#     print(bot.register_next_step_handler(sent_msg, day_handler))
#
#
# def day_handler(message):
#     sign = message.text
#     text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
#     sent_msg = bot.send_message(
#         message.chat.id, text, parse_mode="Markdown")
#     bot.register_next_step_handler(
#         sent_msg, fetch_horoscope, sign.capitalize())
#
#
# def fetch_horoscope(message, sign):
#     day = message.text
#     horoscope = get_daily_horoscope(sign, day)
#     data = horoscope["data"]
#     horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
#     bot.send_message(message.chat.id, "Here's your horoscope!")
#     bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")
#
# #
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    list = message.text.split()
    if list[0] == "f" or list[0] == "F":
        # bot.reply_to(list[1], 'Food and dining')
        bot.send_message(message.chat.id, 'Food and Dining->' + list[1])
    elif list[0] == 't' or list[0] == 'T':
        # bot.reply_to(list[1], 'Transportation')
        bot.send_message(message.chat.id, 'Transportation->' + list[1])
    elif list[0] == 'h' or list[0] == 'H':
        # bot.reply_to(list[1], 'Housing')
        bot.send_message(message.chat.id, 'Housing ->' + list[1])
    elif list[0] == 'e' or list[0] == 'E':
        # bot.reply_to(list[1], 'Entertainment')
        bot.send_message(message.chat.id, 'Entertainment->' + list[1])
    elif list[0] == 'w' or list[0] == 'W':
        # bot.reply_to(list[1], 'Wellness')
        bot.send_message(message.chat.id, 'Wellness->' + list[1])
    elif list[0] == 'p' or list[0] == 'P':
        bot.send_message(message.chat.id, 'Personal care->' + list[1])
    elif list[0] == 'm' or list[0] == 'M':
        # bot.reply_to(list[1], 'Miscellaneous')
        bot.send_message(message.chat.id, 'Miscellaneous->' + list[1])
    else:
        bot.reply_to(message,
        '''
        Invalid command. Please try again, Young Padawan.\n
        Do require any assistance, do not hesitate to call upon me by typing /help. I am always watching
                     
        ''')


bot.infinity_polling()
