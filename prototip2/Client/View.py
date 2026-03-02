class ViewConsole:
    def viewshowMenu(self):
        print("=== MENU ===")
        print("1. Login")
        print("2. Exit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit):
                optionInt=int(option)
                if(option >= 1 and option <= 3):
                    return optionInt
                
            print("Option not valid")
            
    def viewGeneral(self):
        option=-1
        while(option!=2):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #Login
                    self.viewLogin()
                case 2:
                    #Quit
                    print("Adeu, Gracies per utilitzar l'aplicació")
                    
    def viewLogin(self):
        print("View Login")
        print("Introdueix el username o email i el password: ")
        username=input("Username o email: ")
        passwd=input("Password: ")
        #DaouserClient ha de fer login
        #Depennt de la resposta va a Child o User Not Authenticated
            
            
       