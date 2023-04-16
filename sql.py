# import mysql.connector
#
# # Connect to the MySQL database
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Ritvik@1901",
#     database="DarthSaver"
# )
#
# # Create a cursor object to execute SQL queries
# cursor = db.cursor()
#
# # Create the expenses table
# cursor.execute("CREATE TABLE Expenses ("
#                "id INT AUTO_INCREMENT PRIMARY KEY,"
#                "name VARCHAR(255) UNIQUE,"
#                "budget FLOAT,"
#                "food FLOAT,"
#                "transportation FLOAT,"
#                "housing FLOAT,"
#                "entertainment FLOAT,"
#                "wellness FLOAT,"
#                "personal_care FLOAT,"
#                "miscellaneous FLOAT)")
#
# # Commit the changes to the database
# db.commit()
#
# # Close the cursor and database connection
# cursor.close()
# db.close()


import requests


def get_daily_horoscope(sign: str, day: str) -> dict:
    """Get daily horoscope for a zodiac sign.

    Keyword arguments:
    sign:str - Zodiac sign
    day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
    Return:dict - JSON data
    """
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)

    return response.json()