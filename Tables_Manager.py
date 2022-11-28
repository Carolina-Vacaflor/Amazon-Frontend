import Database_Connection

#connection = Database_Connection.conection
#cursor = Database_Connection.cursor

###Product
def registerProduct(id, title, rate, review, price, image):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    query = """INSERT INTO product(id, title, rate, review, price, image, tracker, counter) 
                VALUES('"""+id+"','"+ title +"','"+rate+"','"+review+"','"+price+"','"+image+"',0,0)"
    cursor.execute(query)
    connection.commit()
    connection.close()

# def registerProduct(item):
#     connection = Database_Connection.conection
#     cursor = Database_Connection.cursor
#     query = """INSERT INTO product(id, title, rate, review, price, image, tracker, counter) 
#                 VALUES('"""+item[5]+"','"+ item[0] +"','"+item[1]+"','"+item[2]+"','"+item[3]+"','"+item[4]+"',0,0)"
#     cursor.execute(query)
#     connection.commit()
#     connection.close()

def readProduct(title):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("SELECT * FROM product WHERE title = '"+ title +"'")
    product = cursor.fetchall()
    for row in product:
        print("Title: ", row[1])
        print("Rate: ", row[2])
        print("Review: ", row[3])
        print("Price: ", row[4])
        print("Image: ", row[5])
        print("Tracker: ", row[6])        
        print("Counter: ", row[7])
    connection.commit()
    connection.close()

def updateTracker(tracker, title):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("UPDATE product SET tracker ="+str(tracker)+" WHERE title ='"+title+"'")
    connection.commit()
    connection.close()

def updateCounter(counter, title):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("UPDATE product SET counter ="+str(counter)+" WHERE title ='"+title+"'")
    connection.commit()
    connection.close()
###User
def registerUser(name, lastName, email, password):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    query = "INSERT INTO user(name, lastName, email, password) VALUES('"+name+"','"+lastName+"','"+email+"','"+password+"')"
    cursor.execute(query)
    connection.commit()
    connection.close()

def readAllUsers():
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("SELECT * from user")
    users = cursor.fetchall()
    connection.commit()
    connection.close()
    print(users)

def readUser(email):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("SELECT * from user WHERE email ='"+email+"'")
    user = cursor.fetchall()
    for row in user:
        print("Name:", row[1])
        print("Last Name:", row[2])
        print("Email:", row[3])
        print("Password:", row[4])
    connection.commit()
    connection.close()    

def updateUser(name, email):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("UPDATE user SET name ='"+name+"' WHERE email ='"+email+"'")
    connection.commit()
    connection.close()

def deleteUser(name):
    connection = Database_Connection.conection
    cursor = Database_Connection.cursor
    cursor.execute("DELETE FROM user WHERE name ='"+name+"'")
    connection.commit()
    connection.close()