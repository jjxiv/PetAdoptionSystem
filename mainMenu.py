"""
    File name:
    Authors:
    Description:
    Date:
    Email:
"""

import register, viewPets

def mainMenu():
    print("==========Pet Adoption System==========")
    print("[1] Register")
    print("[2] User Login")
    print("[3] Admin Login")
    print("[4] View Available Pets")
    print("=======================================")
    mm = int(input("Enter a number: "))
    #WARNING: insert validation here
    match mm:
        case 1:
            pass
            # Register Function
            register.registration()
        case 2:
            pass
            #User Login
        case 3:
            pass
            #Admin Login
        case 4:
            pass
            viewPets.availablePets()
            #View Available Pets
        case _:
            pass
            print("Error, try again.")
    pass

if __name__ == "__main__":
    mainMenu()

