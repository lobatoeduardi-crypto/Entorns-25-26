import requests
from User import *
from flask import jsonify

class DaoUserClient:
    base_URL = "http://localhost:5000"
    
    def login(self, user):
        #user.username
        #user.password
        #Agafo username i password del Objecte User
        #Validacio parametres
        #TO-DO
        #Peticio HTTP al WebService/login
        URL_peticio=self.base_URL + "/login"
        params_POST = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_POST)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw["coderesponse"]
            if code_response == '1': #Usuari Validat (self, id, username, password, email, idrole, token)
                user=User(user_data_raw["id"],user_data_raw["username"]
                      ,"",user_data_raw["email"]
                      ,user_data_raw["idrole"], user_data_raw["token"])
            else:
                return None
        else:
            return None
        
        
'''Servei Login
End-point: /login
Method: POST
Estat: Public
Tipus petició : application/json
Paramètres:

username : (string) username o email
password : (string) password
Resposta Usuari validat Ok:
http Response Code: 200 ok

{    
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "token12345",
    "idrole": "2",
    "msg": "Usuari Ok"
    "coderesponse": "1"
}

Resposta Usuari No validat: http Response Code: 400 ok

{
     "coderesponse": "0"
     "msg": "No validat"
}
'''