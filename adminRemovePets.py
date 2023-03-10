
def adminRemovePets():

    try:
        petIDnumber = int(input("Input the Pet ID of the pet you wish to remove:"))
    except:
        input("Invalid input. Please try again.")
        adminRemovePets()

    #retrieve the pet from database
    #display the pet details

    confirmq = input("Remove this pet? [Y/N]")

    match confirmq:
        case "y" | "Y":
            #assign userid to selected pet
            print("Pet has been removed from the listing.")
            input("Press Enter to continue...")
            pass
        case "n" | "N":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            pass
        case _:
            print("Invalid input. Please try again.")
            adminRemovePets()


