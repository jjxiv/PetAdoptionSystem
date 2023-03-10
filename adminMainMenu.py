import mainMenu

#user login module goes here

def adminMainMenu():
    print("==========Pet Adoption System==========")
    print("[1] Add Pets")
    print("[2] Remove Pets")
    print("[3] Modify Pet Information")
    print("[4] Logout")

    userMainMenuSelection = int(input("Enter a number:"))

    match userMainMenuSelection:
        case 1:  #adminAddPets()
            pass
        case 2:  #adminRemovePets()
            pass
        case 3:  #adminModifyPets()
            pass
        case 4:  #userLogout()
            # log out the user
            mainMenu.mainMenu()
            pass
        case _:
            print("Invalid input. Please try again.")
            adminMainMenu()
            pass

adminMainMenu()

