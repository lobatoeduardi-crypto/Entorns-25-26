from flask import Flask, request, jsonify
from DaoServer import UserDAO  # Importamos tu clase DAO

app = Flask(__name__)
dao = UserDAO()

# --- PASO 1 de la pizarra: LOGIN ---
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
        # Si es correcto, devolvemos el token que generó tu DAO
        return jsonify({
            "status": "success",
            "token": user['token'],
            "username": user['username']
        }), 200
    else:
        return jsonify({"status": "error", "message": "Login incorrecto"}), 401

# --- PASO 2 de la pizarra: OBTENER DATOS CON TOKEN ---
@app.route('/getchilds', methods=['GET'])
def get_childs():
    # El cliente envía el token en la URL (ej: /getchilds?token=abc123...)
    token = request.args.get('token')
    
    if not token:
        return jsonify({"error": "Falta el token"}), 400
    
    # Usamos el DAO para buscar los niños vinculados a ese token
    childs = dao.getChildrenByToken(token)
    
    if childs:
        return jsonify(childs), 200
    else:
        return jsonify({"message": "No se encontraron niños o token inválido"}), 404

if __name__ == '__main__':
    # Esto arranca el servidor en el puerto 5000
    app.run(debug=True, port=5000)