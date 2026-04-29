class User:
    def __init__(self, id, username, password, email, idrole, token):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.idrole = idrole 
    
    def __str__(self):
        return f"User(ID: {self.id}, Name: {self.username}, Email: {self.email}, Role: {self.idrole})"