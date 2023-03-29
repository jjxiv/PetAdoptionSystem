"""
    File name:      userAdopt.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the option for a user to adopt
                    a pet that will be stored to user's owned pets.
"""


import os


"""
    Method name:    adopt()
    Parameters:     petsDB, userID
    Return Type:    none
    Description:    A method that contains adopting a pet. In addition,
                    this method saves the ownership in the pets database.
"""
def adopt(petsDB,uID):
    if os.path.exists(petsDB):
        print("The USER ID LOGGED IN IS: ",uID)
        petIDnumber = str(input("Input Pet ID to adopt:"))
        pid = "PetID:" + petIDnumber + "\n"

        with open(petsDB, "r") as f:
            lines = f.readlines()

        if pid in lines:
            temp = []
            valid = False
            # print("Pet information to be adopted: ")
            num = lines.index(pid)
            # print(lines)
            print("The index of Pet id is: ",num)
            checkID = lines[num+1].strip()

            if checkID != "OwnerID:null":
                print("[System] Warning, the pet has an owner already.")
                choice = input("Overwrite the existing owner?[y/n]: ")
                match choice:
                    case "y" | "Y":
                        valid = True
                        pass
                    case "n" | "N":
                        print("[System] Operation cancelled.")
                        pass
                    case _:
                        print("[System] Invalid input. Please try again.")
                        pass
            else:
                print("[System] Proceeding to adoption.")
                valid = True

            if valid:
                for i in range(0,7):
                    temp.append(lines[num+i])

                print("Value of temp:",temp)

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
                    print(pid.strip(), " owner has been modified.")

                f = open(petsDB, "a")
                petID = temp[0]
                ownerIDTemp = uID.replace("UserID:","")
                ownerIDTemp = ownerIDTemp.strip()
                petOwner = "OwnerID:"+ownerIDTemp+"\n"
                petName = temp[2]
                petBreed = temp[3]
                petGender = temp[4]
                petAge = temp[5]
                petPicture = temp[6]

                f.write("\n")
                f.write(petID)
                f.write(petOwner)
                f.write(petName)
                f.write(petBreed)
                f.write(petGender)
                f.write(petAge)
                f.write(petPicture)
                f.close()
            else:
                print("[System] Adoption failed..")

        else:
            print("[System] \"", pid.strip(), "\" does not exist.")
    pass


"""
    Method name:    userAdopt()
    Parameters:     userID
    Return Type:    none
    Description:    A method that contains adopting a pet. This is the
                    main menu for user adoption.
"""
def userAdopt(userID):
    try:
        print("The user is is:",userID)
        condition = True
        print("The value of userid in useradopt is:",userID)
        uID = userID

        while condition:
            print("==========Adopt A Pet==========")
            print("[1] Dogs")
            print("[2] Cats")
            print("[3] Exit")
            choice = int(input("Enter a number:"))

            match choice:
                case 1:
                    petsDB = "dogsDatabase.txt"
                    adopt(petsDB,uID)
                case 2:
                    petsDB = "catsDatabase.txt"
                    adopt(petsDB,uID)
                case 3:
                    condition = False
                case __:
                    print("[System] Invalid user input")
    except Exception as e:
        print("[System] Error encountered")
        print("[System]",e)


