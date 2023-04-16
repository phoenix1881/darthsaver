# # # # # import mysql.connector
# # # # #
# # # # # # Connect to the MySQL database
# # # # # db = mysql.connector.connect(
# # # # #     host="aws.connect.psdb.cloud",
# # # # #     user="afbh24xgk2o21hmz6whi",
# # # # #     password="pscale_pw_xvbgAMySIpeaZyJARIaymDOkcvCrz555lCdnD631ybY",
# # # # #     database="darthvader_bot"
# # # # # )
# # # # # #
# # # # # # # Create a cursor object to execute SQL queries
# # # # # cursor = db.cursor()
# # # # #
# # # # #
# # # # # # Create the expenses table
# # # # # cursor.execute("SELECT * from expenses;")
# # # # # if cursor.execute:
# # # # #   print(True)
# # # # # else:
# # # # #   print(False)
# # # # #
# # # # # # Commit the changes to the database
# # # # # db.commit()
# # # # #
# # # # # # Close the cursor and database connection
# # # # # cursor.close()
# # # # # db.close()
# # # # #
# # # # #
# # # # # # import requests
# # # # #
# # # # #
# # # # # # def get_daily_horoscope(sign: str, day: str) -> dict:
# # # # # #     """Get daily horoscope for a zodiac sign.
# # # # #
# # # # # #     Keyword arguments:
# # # # # #     sign:str - Zodiac sign
# # # # # #     day:str - Date in format (YYYY-MM-DD) OR TODAY OR TOMORROW OR YESTERDAY
# # # # # #     Return:dict - JSON data
# # # # # #     """
# # # # # #     url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
# # # # # #     params = {"sign": sign, "day": day}
# # # # # #     response = requests.get(url, params)
# # # # #
# # # # # #     return response.json()
# # # #
# # # #
# # # # import os
# # # # import MySQLdb
# # # #
# # # # connection = MySQLdb.connect(
# # # #     # host= os.getenv("HOST"),
# # # #     # user=os.getenv("USERNAME"),
# # # #     # passwd= os.getenv("PASSWORD"),
# # # #     # db= os.getenv("DATABASE"),
# # # #     host="aws.connect.psdb.cloud",
# # # #     user="afbh24xgk2o21hmz6whi",
# # # #     passwd="pscale_pw_xvbgAMySIpeaZyJARIaymDOkcvCrz555lCdnD631ybY",
# # # #     db="darthvader_bot",
# # # #     ssl_mode="VERIFY_IDENTITY",
# # # #     ssl={
# # # #         "ca": "/etc/ssl/cert.pem"
# # # #     }
# # # # )
# # #
# # #
# # # import mysql.connector
# # # from mysql.connector import Error
# # #
# # #
# # # connection = mysql.connector.connect(host="aws.connect.psdb.cloud",
# # # user="afbh24xgk2o21hmz6whi",
# # # passwd="pscale_pw_xvbgAMySIpeaZyJARIaymDOkcvCrz555lCdnD631ybY",
# # # db="darthvader_bot",)
# # # if connection.is_connected():
# # #     db_Info = connection.get_server_info()
# # #     print("Connected to MySQL Server version ", db_Info)
# # #     cursor = connection.cursor()
# # #     cursor.execute("select database();")
# # #     record = cursor.fetchone()
# # #     print("You're connected to database: ", record)
# # #
# # #
# #
# #
# # import mysql.connector
# # from mysql.connector import Error
# #
# # connection = mysql.connector.connect(
# #     host="aws.connect.psdb.cloud",
# #     user="afbh24xgk2o21hmz6whi",
# #     passwd="pscale_pw_xvbgAMySIpeaZyJARIaymDOkcvCrz555lCdnD631ybY",
# #     db="darthvader_bot",
# # )
# #
# # if connection.is_connected():
# #     db_Info = connection.get_server_info()
# #     print("Connected to MySQL Server version ", db_Info)
# #     cursor = connection.cursor()
# #     cursor.execute("select database();")
# #     record = cursor.fetchone()
# #     print("You're connected to database: ", record)
# #
# #
#
#
# import mysql.connector
# from mysql.connector import Error, pooling
#
# config = {
#     "host": "aws.connect.psdb.cloud",
#     "user": "afbh24xgk2o21hmz6whi",
#     "password": "pscale_pw_xvbgAMySIpeaZyJARIaymDOkcvCrz555lCdnD631ybY",
#     "database": "darthvader_bot",
#
# }
#
# pool_name = "mypool"
# pool_size = 5
#
# cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name, pool_size=pool_size, **config)
#
#
# connection = cnxpool.get_connection()
#
# if connection.is_connected():
#     db_Info = connection.get_server_info()
#     print("Connected to MySQL Server version ", db_Info)
#     cursor = connection.cursor()
#     cursor.execute("select database();")
#     record = cursor.fetchone()
#     print("You're connected to database: ", record)
#
#     # # Remember to close the cursor and release the connection back to the pool
#     # cursor.close()
#     # connection.close()
