from flask import Flask, request, jsonify
from dataclasses import dataclass, asdict
from DaoServer import UserDAO, ChildDAO

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

# Instantiate DAO
userDao = UserDAO()
childDao = ChildDAO()

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    # Token validation if exists
    token=request.headers.get("api-token")
    user=None
    if(token):
        # comprobar que el token existeix a un usuari
        user=userDao.getUserByToken(token)
    else:
        data = request.get_json()
        identifier = data.get('username') # Username or email
        password = data.get('password')
        user = userDao.login(identifier, password)
        
    if user:
        response = ApiResponse(
            msg="Authenticated",
            coderesponse="1",
            data=user
        )
    else:
        response = ApiResponse(
            msg="Not authenticated",
            coderesponse="0",
            data=""
        )
    return jsonify(asdict(response)), 200

@app.route('/getchilds', methods=['POST'])
def get_childs():
    token = request.args.get('token')
    childs = userDao.getChildrenByToken(token)
    
    if childs:
        response = ApiResponse(
            msg="Children found",
            coderesponse="1",
            data=childs
        )
    else:
        response = ApiResponse(
            msg="No children found or invalid token",
            coderesponse="0",
            data=[]
        )
        
    return jsonify(asdict(response)), 200

@app.route('/child', methods=['POST'])
def child():
    token=request.headers.get("api-token")
    user=None
    if(token):
        # comprobar que el token existeix a un usuari
        user=userDao.getUserByToken(token)
        
    if not user:
        response = ApiResponse(
            msg="Access not granted",
            coderesponse="0",
            data=""
        )
        return jsonify(asdict(response)), 400
    
    data = request.get_json()
    childs=childDao.getChilds(user['id'])
    response = ApiResponse(
        msg="getChilds",
        coderesponse="1",
        data=childs
    )
    return jsonify(asdict(response)), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)