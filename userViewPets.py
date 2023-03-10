import userMainMenu

def userViewPets():
    print("=========Available Pet Details=========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Exit")
    print("=======================================")
    userViewPetsSelection = int(input("Enter a number:"))

    match userViewPetsSelection:
        case 1:  #dogs()
            pass
        case 2:  #cats()
            pass
        case 3:  #userDisplayOwned()
            userMainMenu.userMainMenu()
        case _:
            print("Invalid input. Please try again.")
            userMainMenu()
            pass

userMainMenu()

