import sqlite3

conection = sqlite3.connect("AmazonWebScraperDB.db", check_same_thread=False)
cursor = conection.cursor()