import os
def pets(petsDB):
    print("=======================================")
    print("[1] View Pet Details (Tabular)")
    print("[2] Search for specific criteria of pets")
    print("[3] Exit")
    choice = int(input("Enter a number:"))

    match choice:
        case 1:
            if os.path.exists(petsDB):
                with open(petsDB, "r") as f:
                    text = f.readlines()
                    inner = []
                    outer = []

                    print("{:<20}\t{:<20}\t{:<20}".format(text[0].strip(),text[1].strip(),text[2].strip()), end='')



                    print("\nValue of list in outer:",outer)

            else:
                print("[System] There is no existing records for dogs...")
                pass
        case 2:
            pass
        case __:
            print("[System] Invalid user input")
    pass


def userViewPets():
    print("=========Available Pet Details=========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Exit")
    print("=======================================")
    userViewPetsSelection = input("Enter a number:")

    match userViewPetsSelection:
        case "1":
            petsDB = "dogsDatabase.txt"
            pets(petsDB)
            input("Press Enter to continue...")
            pass
        case "2":
            petsDB = "catsDatabase.txt"
            pets(petsDB)
            input("Press Enter to continue...")
            pass
        case "3":
            pass
        case _:
            print("Invalid input. Please try again.")
            userViewPets()

if __name__ == "__main__":
    userViewPets()


