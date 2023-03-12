import os
def adminRemovePets():
    try:
        dogsDB = "dogsDatabase.txt"
        catsDB = "catsDatabase.txt"
        valid = False

        print("============Remove Pets=============")
        print("[1] - Dogs")
        print("[2] - Cats")
        choice = int(input("Enter a number: "))

        match choice:
            case 1:
                petsDB = dogsDB
                valid = True
            case 2:
                petsDB = catsDB
                valid = True
            case __:
                print("Entered value is invalid: ", choice)

        if valid == True:
            if os.path.exists(petsDB):
                petIDnumber = str(input("Input the Pet ID to remove:"))
                pid = "PetID:" + petIDnumber + "\n"

                with open(petsDB, "r") as f:
                    lines = f.readlines()

                if pid in lines:
                    num = lines.index(pid)
                    if pid == lines[-7]:
                        for i in range(0, 7):
                            del lines[num]
                    else:
                        for i in range(0, 8):
                            del lines[num]

                    with open(petsDB, "w") as f:
                        if lines:
                            if lines[-1] == "\n":
                                del lines[-1]
                        f.writelines(lines)
                        print(pid.strip(), "has been deleted")
                else:
                    print("[System] \"", pid.strip(), "\" does not exist.")
            else:
                print("[System] There is no existing pet database")
        else:
            print("[System] Returning to menu")
    except:
        input("Invalid input. Please try again.")

    #retrieve the pet from database
    #display the pet details

    # confirmq = input("Remove this pet? [Y/N]")
    #
    # match confirmq:
    #     case "y" | "Y":
    #         #assign userid to selected pet
    #         print("Pet has been removed from the listing.")
    #         input("Press Enter to continue...")
    #         pass
    #     case "n" | "N":
    #         print("Operation cancelled.")
    #         input("Press Enter to continue...")
    #         pass
    #     case _:
    #         print("Invalid input. Please try again.")
    #         adminRemovePets()


