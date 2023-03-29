"""
    File name:      userModifyInfo.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the user modification of information
                    for flexibility upon changes. This requires the user to
                    re-login for verification.
"""

import os

"""
    Method name:    userModifyInfo()
    Parameters:     userID
    Return Type:    none
    Description:    A method that contains modifying the user's information.
"""
def userModifyInfo(userID):
    condition = False
    #retrieve user information
    print("============Modify User Information=============")
    print("[System] Login again for verification")
    if os.path.exists("userDatabase.txt"):
        username = []  # usernames from text will be stored in this list
        password = []  # passwords from text file will be stored in this list

        f1 = open("userDatabase.txt", "r+")
        userID = []  # This variable stores the user id's
        text = f1.readline()
        ctr = 0
        while text:
            if ctr%7==0:
                userID.append(text)
            text = f1.readline()
            ctr+=1
        f1.close()

        f = open("userDatabase.txt", "r")
        text = f.readline()  # used for getting the username and password
        fText = open("userDatabase.txt", "r")
        getID = fText.readlines()
        # used for getting the usernameID to assigned as session variable

        while text:
            if "Username:" in text:
                uname = text.replace("Username:", "")
                uname = uname.replace("\n", "")
                username.append(uname)  # append username to list

            elif "Password:" in text:
                pword = text.replace("Password:", "")
                pword = pword.replace("\n", "")
                password.append(pword)  # append password to list
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
                condition = True
                # Obtain user ID from the readlines
                tempUserName = "Username:" + userNameInput + "\n"
                num = getID.index(tempUserName)
                userID = getID[num - 1]
                # userID set as session login variable
                f.close()
                fText.close()
                #userMainMenu(userID)
            else:
                print("[System] Invalid credentials, please try again...")
        else:
            print("[System] Invalid credentials, please try again...")
    else:
        print("[System] No existing user database...")

    if condition:
        uid = userID
        with open("userDatabase.txt", "r") as f:
            lines = f.readlines()

        if uid in lines:
            num = lines.index(uid)
            if uid == lines[-7]:
                for i in range(0, 6):
                    del lines[num]
            else:
                for i in range(0, 7):
                    del lines[num]

            with open("userDatabase.txt", "w") as f:
                if lines:
                    if lines[-1] == "\n":
                        del lines[-1]
                f.writelines(lines)
                print("[System]",uid.strip(),"is going to be modified")
        else:
            print("[System] Cannot find the user id to modify.")

        userName = str(input("Enter new username:"))
        password = str(input("Enter new password:"))
        name = str(input("Enter new name:"))
        emailAddress = str(input("Enter new email address:"))
        birthday = str(input("Enter birthday:"))

        # Display information from user input
        print("=======================================")
        print("Registration information:")
        print("Username:", userName)
        print("Password:", password)
        print("Name:", name)
        print("Email Address:", emailAddress)
        print("Birthday:", birthday)
        print("=======================================")

        confirmq = input("Confirm Changes? [Y/N]")

        match confirmq:
            case "y" | "Y":
                #save changes to db
                f = open("userDatabase.txt", "a")
                if len(userID) > 1:
                    f.write("\n")
                f.write(userID)
                f.write("Username:" + userName + "\n")
                f.write("Password:" + password + "\n")
                f.write("Name:" + name + "\n")
                f.write("EmailAddress:" + emailAddress + "\n")
                f.write("Bday:" + birthday + "\n")
                print("[System] Registration success...")
                f.close()
                pass
            case "n" | "N":
                print("Operation cancelled.")
                input("Press Enter to continue...")
                pass
            case _:
                print("Invalid input. Please try again.")