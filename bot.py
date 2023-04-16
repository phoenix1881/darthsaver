import os

import telebot

import mysql.connector
import random
import string
from datetime import datetime
from mysql.connector import Error, pooling

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


config = {
    "host": "aws.connect.psdb.cloud",
    "user": "45po9rjkuqnael9i7k4v",
    "password": "pscale_pw_ne1u7ya541ROrfBrXoYs0cDW4IYkk4TEeua38bCzSZu",
    "database": "darthvader_bot",

}


'''
HOST=aws.connect.psdb.cloud
USERNAME=45po9rjkuqnael9i7k4v
PASSWORD=pscale_pw_ne1u7ya541ROrfBrXoYs0cDW4IYkk4TEeua38bCzSZu
DATABASE=darthvader_bot
'''

pool_name = "mypool"
pool_size = 10

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **config)


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
    initial_set_Name(message)


@bot.message_handler(commands=['setName'])
def initial_set_Name(message):
    text = "What's your name Young Padawan?"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, initial_name_handler)


def initial_name_handler(message):
    name = message.text
    # create a new user in the database
    # instantiate an new user in SQL
    current_date = datetime.now().date()
    username = random_string(10)
    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM expenses WHERE user_id = %s", (message.chat.id,))
        records = cursor1.fetchall()
        if len(records) == 0:

            cursor = connection.cursor()
            '''insert an user into this table CREATE TABLE expenses (
        
        user_id INT NOT NULL,
        username VARCHAR(255) NOT NULL,
        monthlybudget DECIMAL(10,2) NOT NULL DEFAULT 0,
        foodanddining DECIMAL(10,2) NOT NULL DEFAULT 0,
        transportation DECIMAL(10,2) NOT NULL DEFAULT 0,
        entertainment DECIMAL(10,2) NOT NULL DEFAULT 0,
        housing DECIMAL(10,2) NOT NULL DEFAULT 0,
        wellness DECIMAL(10,2) NOT NULL DEFAULT 0,
        personalcare DECIMAL(10,2) NOT NULL DEFAULT 0,
        misc DECIMAL(10,2) NOT NULL DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (user_id)
    # );'''
    #         cursor.execute()
    #         cursor.execute("INSERT INTO expenses () VALUES (%s)", (name,))
            insert_query = """
            INSERT INTO expenses (
                user_id, date, username, monthlybudget, foodanddining, transportation, entertainment,
                housing, wellness, personalcare, misc
            )
            VALUES (
                %s, %s, %s, 0, 0, 0, 0, 0, 0, 0, 0
            )
            """

            cursor = connection.cursor()
            cursor.execute(insert_query, (message.chat.id, current_date, username))
            connection.commit()
            cursor.close()
            #
            # connection.commit()
            # cursor.close()
            connection.close()
            bot.send_message(message.chat.id, "Your name has been set to " + name + ".")
            set_Budget(message)
        else:
            print("User already exists")
            connection.close()
            bot.send_message(message.chat.id, "You already have an account. Please use /updateName to update your name.")


    return True


@bot.message_handler(commands=['updateName'])
def update_set_Name(message):

    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM expenses WHERE user_id = %s", (message.chat.id,))
        records = cursor.fetchall()
        if len(records) == 0:
            bot.send_message(message.chat.id, "You do not have an account. Please use /setName to set your name.")
        connection.commit()
        cursor.close()
        connection.close()

    text = "What do you want your name updated to Young Padawan? Your current name is " + records[0][2] + "."
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, update_name_handler)


def update_name_handler(message):
    name = message.text
    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE expenses SET username = %s WHERE user_id = %s", (name, message.chat.id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Name updated successfully")
    bot.send_message(message.chat.id, "Your name has updated to " + name + ".")
    return True


@bot.message_handler(commands=['setBudget'])
def set_Budget(message):
    text = "What's your monthly budget Young Padawan?"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, budget_handler)


def budget_handler(message):
    budget = message.text
    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE expenses SET monthlybudget = %s WHERE user_id = %s", (budget, message.chat.id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Budget updated successfully")
    bot.send_message(message.chat.id, "Your monthly budget has been set to " + budget + " rupees.")
    return True


@bot.message_handler(commands=['updateBudget'])
def update_Budget(message):
    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT monthlybudget FROM expenses WHERE user_id = %s", (message.chat.id,))
        # print(cursor.fetchone()[0])
        # arr = cursor.fetchone()[0]
        # convert arr object to string
        # a = ''
        # # for i in arr:
        # #     a += str(i)
        # a = str(arr[0])

        # print(a)
        # print(type(str(arr)))
        # print(type(cursor.fetchone()[0]))
        # print(str(cursor.fetchone()[0]))
        records = cursor.fetchall()
        print(records)
        a=''
        for row in records:
            a = str(row[0])
        print(a)
        connection.commit()
        cursor.close()
        connection.close()
    text = "What do you want your monthly budget to be updated to Young Padawan? " + "Your current monthly budget is " + a + " rupees."
    # text = "What do you want your monthly budget to be updated to Young Padawan?"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, update_budget_handler)


def update_budget_handler(message):
    budget = message.text
    connection = cnxpool.get_connection()
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("UPDATE expenses SET monthlybudget = %s WHERE user_id = %s", (budget, message.chat.id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Budget updated successfully")
    bot.send_message(message.chat.id, "Your monthly budget has been updated to " + budget + " rupees.")
    return True


@bot.message_handler(commands=['deleteAccount'])
def delete_Account(message):
    text = "Are you sure you want to delete your account Young Padawan? (Y/N)"
    sent_msg = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent_msg, delete_account_handler)

def delete_account_handler(message):
    answer = message.text
    if answer == "Y" or answer == "y":
        bot.send_message(message.chat.id, "Your account has been successfully deleted. Please use /start to create a new account to converse with me.")
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("DELETE FROM expenses WHERE user_id = %s", (message.chat.id,))
            connection.commit()
            cursor.close()
            connection.close()
            print("Account deleted successfully")
    elif answer == "N" or answer == "n":
        bot.send_message(message.chat.id, "Your account has not been deleted.")
    else:
        bot.send_message(message.chat.id, "Please enter a valid answer.")
    return True

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
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET foodanddining = %s WHERE user_id = %s", (list[1], message.chat.id))

            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Food and Dining")
        bot.send_message(message.chat.id, 'Food and Dining->' + list[1])
    elif list[0] == 't' or list[0] == 'T':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET transportation = %s WHERE user_id = %s", (list[1], message.chat.id))

            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Transportation")
        bot.send_message(message.chat.id, 'Transportation->' + list[1])
    elif list[0] == 'h' or list[0] == 'H':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET housing = %s WHERE user_id = %s", (list[1], message.chat.id))

            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Housing")
        bot.send_message(message.chat.id, 'Housing ->' + list[1])
    elif list[0] == 'e' or list[0] == 'E':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET entertainment = %s WHERE user_id = %s", (list[1], message.chat.id))
            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Entertainment")
        bot.send_message(message.chat.id, 'Entertainment->' + list[1])
    elif list[0] == 'w' or list[0] == 'W':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            # cursor.execute("UPDATE expenses (user_id, wellness) VALUES (%s, %s)", (message.chat.id, list[1]))
            cursor.execute("UPDATE expenses SET wellness = %s WHERE user_id = %s", (list[1], message.chat.id))
            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Wellness")
        bot.send_message(message.chat.id, 'Wellness->' + list[1])
    elif list[0] == 'p' or list[0] == 'P':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET personalcare = %s WHERE user_id = %s", (list[1], message.chat.id))
            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Personal Care")
        bot.send_message(message.chat.id, 'Personal care->' + list[1])
    elif list[0] == 'm' or list[0] == 'M':
        connection = cnxpool.get_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("UPDATE expenses SET misc = %s WHERE user_id = %s", (list[1], message.chat.id))

            connection.commit()
            cursor.close()
            connection.close()
            print("Record inserted Miscellaneous")
        bot.send_message(message.chat.id, 'Miscellaneous->' + list[1])
    else:
        bot.reply_to(message,
                     '''
        Invalid command. Please try again, Young Padawan.\n
        \nDo require any assistance, do not hesitate to call upon me by typing /help. I am always watching

        ''')


bot.infinity_polling()

# beautifying tasks
# start
#  help
#  error handling

# core functions
# delete expenses
# update expenses
# view options for every category as well as the name and everything
# SQL integration with everything- done with the existing name and budget places

# future actions
# generate insights and reports