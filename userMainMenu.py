"""
    File name:      userMainMenu.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the main menu for user login.It consists
                    of different functions from different python files.
"""


# Imported python files and library
import os
import userViewPets, userAdopt
import userDisplayOwned, userModifyInfo


"""
    Method name:    login()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the login that will validate
                    if a user is allowed to login based on matching the 
                    username and password.
"""
def login():
    print("============User Login=============")
    if os.path.exists("userDatabase.txt"):
        username = [] # usernames from text will be stored in this list
        password = [] # passwords from text file will be stored in this list

        f = open("userDatabase.txt", "r")
        text = f.readline() # used for getting the username and password
        fText = open("userDatabase.txt", "r")
        getID = fText.readlines()
        # used for getting the usernameID to assigned as session variable

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

                # Obtain user ID from the readlines
                tempUserName = "Username:"+userNameInput +"\n"
                num = getID.index(tempUserName)
                userID = getID[num-1]
                # userID set as session login variable

                f.close()
                fText.close()
                userMainMenu(userID)
            else:
                print("[System] Invalid credentials, please try again...")
        else:
            print("[System] Invalid credentials, please try again...")
    else:
        print("[System] No existing user database...")


"""
    Method name:    userMainMenu()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the user main menu for the 
                    user to navigate over the Pet Adoption System.
"""
def userMainMenu(userID):
    condition = True
    # Loop the main menu until condition is set to False
    while condition:
        print("==========Pet Adoption System==========")
        print("[1] Available Pet Details ")
        print("[2] Adopt A Pet")
        print("[3] View All Your Adopted Pets")
        print("[4] Modify User Information")
        print("[5] Logout")
        print("=======================================")
        userMainMenuSelection = int(input("Enter a number:"))

        match userMainMenuSelection:
            case 1:
                # View user pets
                userViewPets.userViewPets()
            case 2:
                # Adopt pets for user
                userAdopt.userAdopt(userID)
            case 3:
                # Display owned pets by user
                userDisplayOwned.userDisplayOwned()
            case 4:
                # Modify user information
                userModifyInfo.userModifyInfo()
            case 5:
                # User logout, returns to mainMenu.py
                condition = False
                print("[System] Program Terminated")
                userID = 0 # clear user session
            case _:
                print("[System] Invalid input, please try again...")