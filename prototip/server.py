from flask import Flask, jsonify, request

class User:
    def __init__(self,username, nom, password, email, rol):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol

    def __str__(self):
        print(self.nom)
#us1=User(username="ama", nom="Rob Halford",password="12345",email="rob@gmail.com", rol="tutor")
#print(us1)
users= [
    User(username="ama", nom="Rob Halford",password="12345",email="rob@gmail.com", rol="tutor"),
    User(username="john", nom="Johm Cannigan",password="12345",email="john@gmail.com", rol="tutor"),
    User(username="maria", nom="Maria Sams",password="12345",email="maria@gmail.com", rol="tutor")
    
]

class UserDao:
    def __init__(self):
        self.users=users
    def getUserByUsername(self,username):

        return "TO-DO"

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":
    # Anar al DAO Server i cercar User per username
    # respondre amb dades Ususari si trobat
        resposta="username=" + username
    else:  #  Si els paràmetres NO ok 
        # respondre error
        resposta="username No Informat"
    
    return resposta


if __name__ == '__main__':
    app.run(debug=True)