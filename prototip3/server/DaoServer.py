from dataclasses import dataclass, asdict
import random
from flask import jsonify
import mysql.connector
import hashlib
from time import time

class UserDAO:
    
    def connectBBDD(self):
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="TapatApp"
    )
        return connection

    def login (self, identifier, password):
        # connexió a BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)  
        query = """
        SELECT * FROM User 
        WHERE (username = %s OR email = %s) AND password = %s
        """
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        token=""
        if user:
            self.setTokenUser(user['username'])
            #print(user)
            user['token'] = token
        cursor.close() 
        con.close()
        return user
    
    def setTokenUser(self, username):
        # connectar BBDD
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # generar Token
        token=self.getHash() #token=self.getHash(username)
        # Update a BBDD camp Token al usuari per username
        print(type(token))
        query = "UPDATE User SET token = '"+ token +"' WHERE username = '"+ username +"'"
        # print(query)
        print(query)
        cursor.execute(query)
        con.commit()
        # Close BBDD
        cursor.close()
        con.close()
        return token

    def getHash(self):
        milliseconds = str(time() * random.randrange(10000))
        data = milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""
    
    def getHash2(self, username):
        milliseconds = str(time() * 1000)
        data=username + milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest() + ""

dao = UserDAO()
u=dao.login("mare", "mare")
print(u)
    