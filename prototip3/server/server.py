from flask import Flask, request, jsonify
from DaoServer import UserDAO 

app = Flask(__name__)
dao = UserDAO()

@app.route('/login', methods=['POST'])
def login(self, identifier, password):
    con = self.connectBBDD()
    cursor = con.cursor(dictionary=True)  
    query = "SELECT * FROM User WHERE (username = %s OR email = %s) AND password = %s"
    cursor.execute(query, (identifier, identifier, password))
    user = cursor.fetchone()

    if user:
        nuevo_token = self.setTokenUser(user['username'])
        user['token'] = nuevo_token  
        
    cursor.close() 
    con.close()
    return user
    
    if user:
        return jsonify({
            "status": "success",
            "token": user['token'],
            "username": user['username']
        }), 200
    else:
        return jsonify({"status": "error", "message": "Login incorrecto"}), 401

@app.route('/getchilds', methods=['GET'])
def get_childs():
   
    token = request.args.get('token')
    
    if not token:
        return jsonify({"error": "Falta el token"}), 400
    
    childs = dao.getChildrenByToken(token)
    
    if childs:
        return jsonify(childs), 200
    else:
        return jsonify({"message": "No se encontraron niños o token inválido"}), 404

if __name__ == '__main__':
   
    app.run(debug=True, port=5000)