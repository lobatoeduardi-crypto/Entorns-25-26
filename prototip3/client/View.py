from User import *
from DaoUserClient import *

class ViewConsole:

    daoClient=DaoUserClient()
    token=""
   
    def viewShowMenu(self):
        print("\n--- MENU ---")
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit()): 
                optionInt=int(option)
                if(optionInt > 0 and optionInt < 6): 
                    return optionInt
            print("Error: Introdueix una opció correcta")
        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    self.viewLogin()
                case 2:
                    self.viewLoginToken(self.token)
                case 3:
                    self.viewChilds(self.token)
                case 4:
                    self.viewTaps(self.token) 
                case 5:
                    print("Adeu, Gràcies per utilitzar l'aplicació")
                    exit()


    def viewChilds(self, token):
        print("View Childs")
        resposta_child=self.daoClient.childToken(token)
        if(resposta_child):
            print(resposta_child)              
        

    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")
        

    def viewTaps(self, token):
        print("\n--- VIEW TAPS ---")
        if not token:
            print("Error: Primero debes hacer Login (Opción 1) para tener un Token.")
            return

        resposta_taps = self.daoClient.getTaps(token) 
        
        if resposta_taps and 'data' in resposta_taps:
            print(f"Mensaje: {resposta_taps['msg']}")
            print("-" * 40)
            for tap in resposta_taps['data']:
                print(f"ID Tap: {tap['id']} | Fecha: {tap['init']}")
            print("-" * 40)
        else:
            print("No se han encontrado Taps o el Token no es válido.")


viewConsole=ViewConsole()

viewConsole.viewGeneral()
     