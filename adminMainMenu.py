import mainMenu
import adminAddPets
import adminRemovePets
import adminModifyPets
import os

#user login module goes here

def login():
    print("============Admin Login=============")
    if os.path.exists("adminDatabase.txt"):
        username = []
        password = []

        f = open("adminDatabase.txt", "r")
        text = f.readline()

        while text:
            if "Username:" in text:
                uname = text.replace("Username:","")
                uname = uname.replace("\n", "")
                username.append(uname)
            elif "Password:" in text:
                pword = text.replace("Password:","")
                pword = pword.replace("\n", "")
                password.append(pword)
            text = f.readline()

        userNameInput = str(input("Enter username: "))

        if userNameInput in username:
            userPasswordInput = str(input("Enter password: "))
            uIndex = username.index(userNameInput)
            pIndex = password[uIndex]

            if userPasswordInput == pIndex:
                print("Successful Login")
                adminMainMenu()
            else:
                print("Invalid credentials")
        else:
            print("Invalid credentials")

    else:
        print("[System] There is no existing admin database")


def adminAddPets():
    dogsDB = "dogsDatabase.txt"
    catsDB = "catsDatabase.txt"
    valid = False

    print("============Add Pets=============")
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
            print("Entered value is invalid: ",choice)



    if valid == True:
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
                lastID = petID[-1]
                lastID = lastID.replace("PetID:", "")
                lastID = str(int(lastID) + 1)
                f.write("\n")
                f.write("PetID:" + lastID + "\n")
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
        print("Returning to menu")

def adminMainMenu():
    condition = True
    while condition:
        print("======Pet Adoption System - Admin======")
        print("[1] Add Pets")
        print("[2] Remove Pets")
        print("[3] Modify Pet Information")
        print("[4] Logout")
        userMainMenuSelection = int(input("Enter a number:"))
        match userMainMenuSelection:
            case 1:
                adminAddPets()
            case 2:
                adminRemovePets.adminRemovePets()
            case 3:
                adminModifyPets.adminModifyPets()
            case 4:  #userLogout()
                # log out the user
                condition = False
                print("[System] Program Terminated")
                # CLEAR login token
            case _:
                print("Invalid input. Please try again.")
