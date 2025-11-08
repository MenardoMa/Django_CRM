import mysql.connector

#DATABASE
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject = dataBase.cursor()

#CREATE
cursorObject.execute('CREATE DATABASE elderco')

print("All Done!")