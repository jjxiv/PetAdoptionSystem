"""
    File name:      adminModifyPets.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the method for modifying pets information.
                    This method is only handled by the administrator upon access
                    of these privileges.
"""


# Imported os library
import os


"""
    Method name:    adminModifyPets()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the modifying the pet's information
                    and saves the modified information to the database.
"""
def adminModifyPets():
    try:
        dogsDB = "dogsDatabase.txt"
        catsDB = "catsDatabase.txt"
        valid = False

        print("============Modify Pets=============")
        print("[1] - Dogs")
        print("[2] - Cats")
        choice = int(input("Enter a number: "))

        # Switch case will check the corresponding database
        match choice:
            case 1:
                petsDB = dogsDB
                valid = True
            case 2:
                petsDB = catsDB
                valid = True
            case __:
                print("Entered value is invalid: ", choice)

        # Checks the pet id and deletes from the text file
        if valid == True:
            if os.path.exists(petsDB):
                petIDnumber = str(input("Input the Pet ID to modify:"))
                pid = "PetID:" + petIDnumber + "\n"

                with open(petsDB, "r") as f:
                    lines = f.readlines()

                if pid in lines:
                    temp = pid
                    tempList = [] # for debugging
                    print("Pet information to be modified: ")
                    num = lines.index(pid)
                    if pid == lines[-7]:
                        for i in range(0, 7):
                            print(lines[num], end="")
                            tempList.append(lines[num+i])
                        for j in range(0,7):
                            del lines[num]
                    else:
                        for i in range(0, 8):
                            tempList.append(lines[num+i])
                        for j in range(0,8):
                            del lines[num]

                    with open(petsDB, "w") as f:
                        if lines:
                            if lines[-1] == "\n":
                                del lines[-1]
                                pass
                        f.writelines(lines)
                        print("[System]",pid.strip(), "is going to be modified")

                    # Add the information again
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

                        # print("PetID values:", petID)
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

                    petID = tempList[0]
                    ownerID = tempList[1]
                    petName = "Name:"+str(input("Enter Pet Name: "))
                    petBreed = "Breed:"+str(input("Enter Pet Breed: "))
                    petGender = "Gender:"+str(input("Enter Pet Gender: "))
                    petAge = "Age:"+str(input("Enter Pet Age: "))
                    petPicture = "Picture:"+str(input("Enter Pet Picture: "))
                    print()

                    print("=======================================")
                    print("Registration information:")
                    print(petName)
                    print(petBreed)
                    print(petGender)
                    print(petAge)
                    print(petPicture)
                    print("=======================================")
                    input("Press Enter to continue...")

                    # User will input if the modification should be saved
                    confirmq = input("Save modification? [Y/N]")

                    match confirmq:
                        case "y" | "Y":
                            f.write(ownerID)
                            f.write(petName+"\n")
                            f.write(petBreed+"\n")
                            f.write(petGender+"\n")
                            f.write(petAge+"\n")
                            f.write(petPicture+"\n")
                            print("[System] Modification success...")
                        case "n" | "N":
                            print("[System] Modification cancelled...")
                            pass
                        case _:
                            print("[System] Invalid input, please try again...")
                    f.close()
                else:
                    print("[System] \"", pid.strip(), "\" does not exist.\n")
            else:
                print("[System] There is no existing pet database")
        else:
            print("[System] Returning to menu")

    except Exception as e:
        print("[System] Error encountered")
        print("[System]", e)

