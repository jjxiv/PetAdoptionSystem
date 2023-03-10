import userMainMenu

def userAdopt():
    petIDnumber = int(input("Input the Pet ID of the pet you wish to adopt:"))

    #retrieve the pet from database
    #display the pet details

    confirmq = input("Adopt this pet? [Y/N]")

    match confirmq:
        case "y" | "Y":
            #assign userid to selected pet
            #among
            print("Pet has been added to your listing.")
            input("Press Enter to continue...")
            pass
        case "n" | "N":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            pass
        case _:
            print("Invalid input. Please try again.")
            userAdopt()

userMainMenu()

