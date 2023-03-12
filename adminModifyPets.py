import os, adminMainMenu
def adminModifyPets():
    try:
        dogsDB = "dogsDatabase.txt"
        catsDB = "catsDatabase.txt"
        valid = False

        print("============Modify Pets=============")
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
                petIDnumber = str(input("Input the Pet ID to modify:"))
                pid = "PetID:" + petIDnumber + "\n"

                with open(petsDB, "r") as f:
                    lines = f.readlines()

                if pid in lines:
                    temp = pid
                    print("Pet information to be modified: ")
                    num = lines.index(pid)
                    if pid == lines[-7]:
                        for i in range(0, 7):
                            print(lines[num], end="")
                            del lines[num]
                    else:
                        for i in range(0, 8):
                            del lines[num]

                    with open(petsDB, "w") as f:
                        if lines:
                            if lines[-1] == "\n":
                                del lines[-1]
                        f.writelines(lines)
                        print(pid.strip(), "is going to be modified")

                    # Add the information again:

                    print("============Modify Information Pets=============")
                    if os.path.exists(petsDB):
                        print("[System] Retrieving existing files")
                        f = open(petsDB, "r+")
                        petID = []
                        text = f.readline()

                        while text:
                            if "PetID:" in text:
                                petID.append(text)
                            text = f.readline()

                        print("PetID values:", petID)
                        print("")
                        if petID:
                            lastID = str(temp)
                            f.write("\n")
                            f.write(lastID)
                        else:
                            f.write("PetID:1\n")


                    else:
                        print("[System] Creating a new file")
                        f = open(petsDB, "w")
                        f.write("PetID:" + "1\n")
                        pass

                    petName = str(input("Enter Pet Name: "))
                    petBreed = str(input("Enter Pet Breed: "))
                    petGender = str(input("Enter Pet Gender: "))
                    petAge = str(input("Enter Pet Age: "))
                    petPicture = str(input("Enter Pet Picture: "))
                    print()

                    print("Registration information:")
                    print("Pet Name:", petName)
                    print("Pet Breed:", petBreed)
                    print("Pet Gender:", petGender)
                    print("Pet Age:", petAge)
                    print("Pet Picture:", petPicture)
                    print("=======================================")
                    input("Press Enter to continue...")

                    f.write("OwnerID:null\n")
                    f.write("Name:" + petName + "\n")
                    f.write("Breed:" + petBreed + "\n")
                    f.write("Gender:" + petGender + "\n")
                    f.write("Age:" + petAge + "\n")
                    f.write("Picture:" + petPicture + "\n")
                    f.close()

                else:
                    print("[System] \"", pid.strip(), "\" does not exist.")
            else:
                print("[System] There is no existing pet database")
        else:
            print("Returning to menu")
    except:
        input("Invalid input. Please try again.")



    # confirmq = input("Confirm Changes? [Y/N]")



    # match confirmq:
    #     case "y" | "Y":
    #         # save changes to db
    #         print("Information successfully updated.")
    #         input("Press Enter to continue...")
    #         pass
    #     case "n" | "N":
    #         print("Operation cancelled.")
    #         input("Press Enter to continue...")
    #         pass
    #     case _:
    #         print("Invalid input. Please try again.")
    #         adminModifyPets()