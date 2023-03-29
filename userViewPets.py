"""
    File name:      userViewPets.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the displayed pets for user logged in.
                    This enables the user to view pet details in tabular form
                    or view pets based on a specific criteria.
"""

# Imported python library
import os

"""
    Method name:    pets()
    Parameters:     petsDB, userID
    Return Type:    none
    Description:    A method that contains the pets method that allows user
                    to view pets and search for specific type of pets.
"""
def pets(petsDB,userID):
    print("=======================================")
    print("[1] View Pet Details (Tabular)")
    print("[2] Search for specific criteria of pets")
    print("[3] Exit")
    choice = int(input("Enter a number:"))

    match choice:
        case 1:
            vpTabular(petsDB,userID)
            pass
        case 2:
            specificCriteria(petsDB, userID)
            pass
        case 3:
            pass
        case __:
            print("[System] Invalid user input")


"""
    Method name:    vpTabular()
    Parameters:     petsDB, userID
    Return Type:    none
    Description:    A method that contains the tabular form when 
                    displaying the pets information.
"""
def vpTabular(petsDB,userID):
    parts = userID.split(":")
    userID = int(parts[1])

    headers = ["Pet ID", "Owner ID", "Name", "Breed", "Gender", "Age", "Photo"]
    print("\n===================================================================")
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*headers))

    # retrieve dogs owned by user
    if os.path.exists(petsDB):
        f = open(petsDB, "r")

        lines = f.readlines()
        lines = [line.strip('\n').strip() for line in lines]
        lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
        chunks = []
        for i in range(0, len(lines), 8):
            chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
            if chunk[1] == "null":
                chunks.append(chunk)

        if len(chunks) == 0:
            print("No pets owned by this user.")
        else:

            print("-------------------------------------------------------------------")
            for chunk in chunks:
                print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))

    else:
        open("dogsDatabase.txt", "x")

    input("Press enter to continue.")
    pass


"""
    Method name:    specificCriteria()
    Parameters:     petsDB, userID
    Return Type:    none
    Description:    A method that contains the specific criteria for 
                    searching a pet.
"""
def specificCriteria(petsDB,userID):
    criteria = 0
    valid = False
    print("=======================================")
    print("[1] Breed")
    print("[2] Gender")
    print("[3] Age")
    print("[4] Exit")
    choice = int(input("Enter a number:"))

    match choice:
        case 1:
            criteria = 3
            valid = True
            uinput = input("Enter breed:")
            pass
        case 2:
            criteria = 4
            valid = True
            uinput = input("Enter gender:")
            pass
        case 3:
            criteria = 5
            valid = True
            uinput = input("Enter age:")
            pass
        case 4:
            pass
        case __:
            print("[System] Invalid user input")

    if valid:
        parts = userID.split(":")
        userID = int(parts[1])

        headers = ["Pet ID", "Owner ID", "Name", "Breed", "Gender", "Age", "Photo"]
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*headers))

        # retrieve dogs owned by user
        if os.path.exists(petsDB):
            f = open(petsDB, "r")

            lines = f.readlines()
            lines = [line.strip('\n').strip() for line in lines]
            lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
            chunks = []
            for i in range(0, len(lines), 8):
                chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
                if chunk[criteria]==uinput:
                    chunks.append(chunk)

            if len(chunks) == 0:
                print("No pets owned by this user.")
            else:
                for chunk in chunks:
                    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))

        else:
            open("dogsDatabase.txt", "x")
    else:
        pass


"""
    Method name:    userViewPets()
    Parameters:     userID
    Return Type:    none
    Description:    A method that contains the menu for user view pets.
"""
def userViewPets(userID):
    print("=========Available Pet Details=========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Exit")
    print("=======================================")
    choice = int(input("Enter a number:"))

    match choice:
        case 1:
            petsDB = "dogsDatabase.txt"
            pets(petsDB,userID)
            input("Press Enter to continue...")
            pass
        case 2:
            petsDB = "catsDatabase.txt"
            pets(petsDB,userID)
            input("Press Enter to continue...")
            pass
        case 3:
            pass
        case _:
            print("Invalid input. Please try again.")