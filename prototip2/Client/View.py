class ViewConsole:
    def viewshowMenu(self):
        print("=== MENU ===")
        print("1. Login")
        print("2. Exit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit):
                optionInt=int(option)
                if(option > 0 and option < 2):
                    return optionInt
                else:
                    print("Option not valid")
            
       