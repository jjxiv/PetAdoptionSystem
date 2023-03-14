import os, userMainMenu

def adopt(petsDB,uID):
    if os.path.exists(petsDB):
        print("The USER ID LOGGED IN IS: ",uID)
        petIDnumber = str(input("Input Pet ID to adopt:"))
        pid = "PetID:" + petIDnumber + "\n"

        with open(petsDB, "r") as f:
            lines = f.readlines()

        if pid in lines:
            temp = []
            print("Pet information to be adopted: ")
            num = lines.index(pid)
            print(lines)
            print("The index of Pet id is: ",num)
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
                print(pid.strip(), "has been deleted, now needs to be modified [DELETE THIS]")


            """
            PetID:1
            OwnerID:null
            Name:pp
            Breed:pp
            Gender:pp
            Age:pp
            Picture:pp
            """



            f = open(petsDB, "a")

            petID = temp[0]
            ownerIDTemp = uID.replace("UserID:","")
            petOwner = "OwnerID:"+str(ownerIDTemp)
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
            print("[System] \"", pid.strip(), "\" does not exist.")
    pass

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
                    print("Entered value is invalid: ", choice)
            # confirmq = input("Adopt this pet? [Y/N]")
            # match confirmq:
            #     case "y" | "Y":
            #         # assign userid to selected pet
            #         print("Pet has been added to your listing.")
            #         input("Press Enter to continue...")
            #         pass
            #     case "n" | "N":
            #         print("Operation cancelled.")
            #         input("Press Enter to continue...")
            #         pass
            #     case _:
            #         print("Invalid input. Please try again.")
    except Exception as e:
        print("Error encountered")
        print(e)

# userAdopt()

