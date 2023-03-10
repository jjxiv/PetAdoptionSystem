
def userViewPets():
    print("=========Available Pet Details=========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Exit")
    print("=======================================")
    userViewPetsSelection = input("Enter a number:")

    match userViewPetsSelection:
        case "1":  #dogs()
            input("Press Enter to continue...")
            pass
        case "2":  #cats()
            input("Press Enter to continue...")
            pass
        case "3": pass
        case _:
            print("Invalid input. Please try again.")
            userViewPets()


