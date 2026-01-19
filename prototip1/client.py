import requests

class User:
    def __init__(self,username, nom, password, email, rol):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol

    def __str__(self):
        return (self.nom + " " + self.email + " " + self.rol)

class daoUserClient: 
    def getUserByUsername(self, username):
        # Petició Http al WebService (request)
        response = requests.get("http://localhost:5000/user?username=" + username)
        # Si la petició OK code response == 200
        if response.status_code == 200:
            # Obtener json
            user_data_raw = response.json()
            # Crear objecte User si ha trobat
            if 'msg' in user_data_raw.keys():
                return None
            # Si no ha trobat retornar None
            else:
                user=User(user_data_raw['username'], user_data_raw['nom'],
                          user_data_raw['password'], user_data_raw['email'], 
                          user_data_raw['rol'])
                return user
            
        return None
    
class ViewConsole:
    def getInputUsername():
        #TO-DO
        return None
    def showUserInfo(username):
        #TO-DO
        return None
    

'''daoUserClient = daoUserClient()
u=daoUserClient.getUserByUsername("rob")
print(u.nom, u.email, u.rol)
u=daoUserClient.getUserByUsername("NOTEXIST")
print(u)'''

# TO-DO Menú veure tots els usuaris, consultar usuari, add usuari, eliminar usuari

class ViewConsole:

    @staticmethod
    def pedirUsuario():
        return input("Usuario: ")

    @staticmethod
    def mostrarResultado(user):
        if user is None:
            print("No encontrado")
        else:
            print("Encontrado:", user.nom)

dao = daoUserClient()

username = ViewConsole.pedirUsuario()
user = dao.getUserByUsername(username)

ViewConsole.mostrarResultado(user)





