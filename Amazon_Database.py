import sqlite3

conection = sqlite3.connect("AmazonWebScraperDB.db")

cursor = conection.cursor()

cursor.execute(
    """CREATE TABLE product(
        id TEXT, 
        title TEXT, 
        rate TEXT, 
        review TEXT, 
        price TEXT, 
        image TEXT,
        tracker INTEGER,
        counter INTEGER
        )""")

cursor.execute(
    """CREATE TABLE user(
        idUser INTEGER PRIMARY KEY AutoIncrement,
        name TEXT,
        lastName TEXT,
        email TEXT,
        password TEXT)""")

conection.commit()
conection.close()