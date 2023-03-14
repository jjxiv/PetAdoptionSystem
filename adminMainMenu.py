"""
    File name:      userMainMenu.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the main menu for user login.It consists
                    of different functions from different python files.
"""

# Imported python files and library
import adminAddPets, adminRemovePets
import adminModifyPets, os

"""
    Method name:    login()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the login that will validate
                    an admin's privileges and is allowed to login based 
                    on matching the username and password.
"""
def login():
    print("============Admin Login=============")
    if os.path.exists("adminDatabase.txt"):
        username = [] # usernames from text will be stored in this list
        password = [] # passwords from text file will be stored in this list

        f = open("adminDatabase.txt", "r")
        text = f.readline() # used for getting the username and password

        while text:
            if "Username:" in text:
                uname = text.replace("Username:","")
                uname = uname.replace("\n", "")
                username.append(uname) # append username to list
            elif "Password:" in text:
                pword = text.replace("Password:","")
                pword = pword.replace("\n", "")
                password.append(pword) # append password to list
            text = f.readline()

        userNameInput = str(input("Enter username: "))
        if userNameInput in username:
            # checks if username input matches username
            userPasswordInput = str(input("Enter password: "))
            uIndex = username.index(userNameInput)
            pIndex = password[uIndex]

            if userPasswordInput == pIndex:
                # checks if password input matches password
                print("Successful Login")
                adminMainMenu()
                f.close()
            else:
                print("[System] Invalid credentials, please try again...")
        else:
            print("[System] Invalid credentials, please try again...")
    else:
        print("[System] No existing admin database...")

"""
    Method name:    adminAddPets()
    Parameters:     none
    Return Type:    none
    Description:    A method that adds the pets based on dogs or cats
                    that will store separately on different files. The 
                    admin has the allowed privileges to add pets.
"""
def adminAddPets():
    dogsDB = "dogsDatabase.txt"
    catsDB = "catsDatabase.txt"
    valid = False

    # Choice for dogs or cats to add
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
            print("[System] Invalid input...")

    # If the choice above is valid, then the admin can add pets
    if valid == True:
        if os.path.exists(petsDB):
            print("[System] Retrieving existing files")
            f = open(petsDB, "r+")
            petID = [] # Store here the pet id's
            text = f.readline()

            # check pet id's and add them to the list
            while text:
                if "PetID:" in text:
                    petID.append(text)
                text = f.readline()
            print()

            if petID:
                lastID = petID[-1]
                # !!!WARNING!!!
                # Note: replace the line above with the greatest
                # pet ID not the latest
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

        # Display information from admin input
        print("=======================================")
        print("Registration information:")
        print("Pet Name:", petName)
        print("Pet Breed:", petBreed)
        print("Pet Gender:", petGender)
        print("Pet Age:", petAge)
        print("Pet Picture:", petPicture)
        print("=======================================")
        input("Press Enter to continue...")

        # User will input if the registration should be saved
        confirmq = input("Save registration? [Y/N]")
        match confirmq:
            case "y" | "Y":
                f.write("OwnerID:null\n")
                f.write("Name:" + petName + "\n")
                f.write("Breed:" + petBreed + "\n")
                f.write("Gender:" + petGender + "\n")
                f.write("Age:" + petAge + "\n")
                f.write("Picture:" + petPicture + "\n")
                print("[System] Registration success...")
            case "n" | "N":
                print("[System] Registration cancelled...")
                pass
            case _:
                print("[System] Invalid input, please try again...")
        input("Press Enter to continue...")
        f.close()
    else:
        print("[System] Unsuccessful, returning to main menu...")


def adminMainMenu():
    condition = True
    # Loop the main menu until condition is set to False
    while condition:
        print("======Pet Adoption System - Admin======")
        print("[1] Add Pets")
        print("[2] Remove Pets")
        print("[3] Modify Pet Information")
        print("[4] Logout")
        print("=======================================")
        choice = int(input("Enter a number:"))

        match choice:
            case 1:
                # Register Function
                # !!!WARNING!!!
                # Note: Delete adminAddPets.py file in github master repo
                # If done, delete this comment and the comment above
                # Add pets
                adminAddPets()
            case 2:
                # Remove pets
                adminRemovePets.adminRemovePets()
            case 3:
                # Modify pets
                adminModifyPets.adminModifyPets()
            case 4:
                # Log out
                condition = False
                print("[System] Returning to main menu")
            case _:
                print("Invalid input. Please try again.")
