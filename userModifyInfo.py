import os

def userModifyInfo():
    condition = False
    #retrieve user information
    print("============Modify User Information=============")
    print("[System] Login again for verification")
    if os.path.exists("userDatabase.txt"):
        username = []  # usernames from text will be stored in this list
        password = []  # passwords from text file will be stored in this list

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
                userMainMenu(userID)
            else:
                print("[System] Invalid credentials, please try again...")
        else:
            print("[System] Invalid credentials, please try again...")
    else:
        print("[System] No existing user database...")

    if condition:
        Username = str(input("Enter new username:"))
        Password = str(input("Enter new password:"))
        Name = str(input("Enter new name:"))
        EmailAddress = str(input("Enter new email address:"))
        Bday = str(input("Enter new bday:"))





    birthday = str(input("Enter birthday:"))

    print("Username: ", userName)
    print("Password: ", password)
    print("Name: ", name)
    print("Email Address: ", emailAddress)
    print("Birthday: ", birthday)

    confirmq = input("Confirm Changes? [Y/N]")

    match confirmq:
        case "y" | "Y":
            #save changes to db
            print("Information successfully updated.")
            input("Press Enter to continue...")
            pass
        case "n" | "N":
            print("Operation cancelled.")
            input("Press Enter to continue...")
            pass
        case _:
            print("Invalid input. Please try again.")
            userModifyInfo()