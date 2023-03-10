
def adminAddPets():

    #check current list of pets and assign id
    #petID = w/e
    petName = str(input("Enter pet name:"))
    petBreed = str(input("Enter pet breed:"))
    petGender = str(input("Enter pet gender:"))
    petAge = str(input("Enter pet age:"))
    petPhoto = str(input("Enter pet photo:"))

    print("Pet Name: ", petName)
    print("Breed: ", petBreed)
    print("Gender: ", petGender)
    print("Age: ", petAge)
    print("Photo: ", petPhoto)

    confirmq = input("Confirm Changes? [Y/N]")

    match confirmq:
        case "y" | "Y":
            # save changes to db
            print("Information successfully updated.")
            input("Press Enter to continue...")
            pass
        case "n" | "N":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            pass
        case _:
            print("Invalid input. Please try again.")
            adminAddPets()