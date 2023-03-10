import mainMenu
import userViewPets
import userAdopt
import userDisplayOwned
import userModifyInfo

#user login module goes here

def userMainMenu():
    print("==========Pet Adoption System==========")
    print("[1] Available Pet Details ")
    print("[2] Adopt A Pet")
    print("[3] View All Your Adopted Pets")
    print("[4] Modify User Information")
    print("[5] Logout")
    print("=======================================")
    userMainMenuSelection = int(input("Enter a number:"))

    match userMainMenuSelection:
        case 1:
            userViewPets.userViewPets()
            pass
        case 2:
            userAdopt.userAdopt()
            pass
        case 3:
            userDisplayOwned.userDisplayOwned()
            pass
        case 4:
            userModifyInfo.userModifyInfo()
            pass
        case 5:  #userLogout()
            # log out the user
            mainMenu.mainMenu()
            pass
        case _:
            print("Invalid input. Please try again.")
            pass

userMainMenu()

