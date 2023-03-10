import mainMenu


def userMainMenu():
    print("[1] Available Pet Details ")
    print("[2] Adopt A Pet")
    print("[3] View All Your Adopted Pets")
    print("[4] Modify User Information")
    print("[5] Logout")
    userMainMenuSelection = int(input("Enter a number:"))

    match userMainMenuSelection:
        case 1:  #userViewPets()
            pass
        case 2:  #userAdopt()
            pass
        case 3:  #userDisplayOwned()
            pass
        case 4:  #userModifyInfo()
            pass
        case 5:  #userLogout()
            # log out the user
            mainMenu.MainMenu()
            pass
        case _:
            print("Invalid input. Please try again.")
            userMainMenu()
            pass



userMainMenu()