import sqlite3

class Product_Repository:
   
    def __init__(self):
        pass

    def register_product(self,product):
        connection = sqlite3.connect("AmazonWebScraperDB.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO 'product' VALUES('"+product.id+"','"+product.title+"','"+product.rate+"','"+product.review+"','"+product.price+"','"+ product.img+ "',0,0)")
        connection.commit()
        connection.close()
    
    def get_product(self, id):
        connection = sqlite3.connect("AmazonWebScraperDB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product WHERE id = '"+ id +"'")
        cursor.rowcount 
        connection.commit()
        connection.close()

    def updateTracker(self, tracker, id):
        connection = sqlite3.connect("AmazonWebScraperDB.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE product SET tracker ="+str(tracker)+" WHERE id ='"+id+"'")
        connection.commit()
        connection.close()
