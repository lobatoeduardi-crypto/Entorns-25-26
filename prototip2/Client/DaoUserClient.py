import requests
from User import User

class DaoUserClient:
    base_URL = "http://localhost:5000"
    
    def login(self, user):
        URL_peticio = self.base_URL + "/login"
        params_POST = {"username": user.username, "password": user.password}
        
        try:
            response = requests.post(URL_peticio, json=params_POST)
            if response.status_code == 200:
                res_json = response.json()
                
                if str(res_json.get("coderesponse")) == '1':
                    # ENTRAR EN LA CAJA 'data'
                    u_data = res_json.get("data") 
                    return User(
                        u_data.get("id"),
                        u_data.get("username"),
                        "", 
                        u_data.get("email"),
                        u_data.get("idrole")
                    )
            return None
        except:
            return None

    # ESTA ES LA FUNCIÓN QUE TE DABA EL ERROR ROJO
    def get_childs(self, user_id):
        URL = self.base_URL + "/child"
        payload = {"id_user": user_id} # Tal como pide tu server.py
        try:
            response = requests.post(URL, json=payload)
            if response.status_code == 200:
                res_json = response.json()
                # Devolvemos la lista de niños que está en 'data'
                return res_json.get("data", [])
            return []
        except:
            return []
        
if __name__ == "__main__":
    daoClient = DaoUserClient()
    user = User("", "mare", "12345", "", "")
    resposta = daoClient.login(user)
    print(resposta)
        
        
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