import os
#for screen clearing

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
    userMainMenuSelection = input("Enter a number:")

    match userMainMenuSelection:
        case "1":
            userViewPets.userViewPets()
            userMainMenu()
        case "2":
            userAdopt.userAdopt()
            userMainMenu()
        case "3":
            userDisplayOwned.userDisplayOwned()
            userMainMenu()
        case "4":
            userModifyInfo.userModifyInfo()
            userMainMenu()
        case "5":  #userLogout()
            # log out the user
            mainMenu.mainMenu()
            userMainMenu()
        case _:
            print("Invalid input. Please try again.")
            pass

userMainMenu()

