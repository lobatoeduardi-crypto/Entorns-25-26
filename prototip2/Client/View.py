from User import User
from DaoUserClient import DaoUserClient
class ViewConsole:
    
    def __init__(self):
        self.daoClient = DaoUserClient()
      
    def viewShowMenu(self):
        print("=== MENU ===")
        print("1. Login")
        print("2. Exit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit()):
                optionInt=int(option)
                if(optionInt >= 1 and optionInt <= 2):
                    return optionInt
                
            print("Error, Introdueix una opció correcta")
            
    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowMenu()
            match option:
                case 1:
                
                    self.viewLogin()
                case 2:
                    
                    print("Adeu, Gracies per utilitzar l'aplicació")
                    
    def viewLogin(self):
        print("\n--- View Login ---")
        username = input("Username o email: ")
        passwd = input("Password: ")
      
        user_input = User("", username, passwd, "", "") 
        resposta_user = self.daoClient.login(user_input)
        
        if resposta_user:
            self.viewUser(resposta_user) # Ahora saldrá 'mare' y no 'None'
            
            # Pedimos los niños al servidor
            print("Buscant nens a càrrec...")
            llista_nens = self.daoClient.get_childs(resposta_user.id)
            self.viewChilds(llista_nens)
        else:
            self.viewUserNotAutenticated()
            
    def viewChilds(self, childs):
        print("\n--- LLISTA DE NENS (CHILDS) ---")
        if not childs:
            print("No s'han trobat nens per a aquest usuari.")
        else:
            for c in childs:
                # 'child_name' es el nombre que pusiste en dadesServer.py
                print(f"ID: {c.get('id')} | Nom: {c.get('child_name')} | Dorm: {c.get('sleep_average')}h")
            
    def viewUser(self, user):
        print("\n[OK] Usuari Autenticat:")
        print(user)


    def viewUserNotAutenticated(self):
        print("\n[ERROR] Credencials incorrectes")
        
        
if __name__ == "__main__":
    viewConsole=ViewConsole()
    
    viewConsole.viewGeneral()
    
    
        
    
    
        #DaouserClient ha de fer login
        #Depennt de la resposta va a Child o User Not Authenticated
            
            
       