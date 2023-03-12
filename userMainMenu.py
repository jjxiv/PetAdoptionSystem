import mainMenu, os
import userViewPets
import userAdopt
import userDisplayOwned
import userModifyInfo

#user login module goes here
def login():
    print("============User Login=============")
    if os.path.exists("userDatabase.txt"):
        username = []
        password = []

        f = open("userDatabase.txt", "r")
        text = f.readline()
        ctr = 1

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
                userMainMenu()
            else:
                print("Invalid credentials")
        else:
            print("Invalid credentials")

    else:
        print("[System] There is no existing user database")


def userMainMenu():
    condition = True

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
                userViewPets.userViewPets()
                print("went here!!!!")
            case 2:
                userAdopt.userAdopt()

            case 3:
                userDisplayOwned.userDisplayOwned()
            case 4:
                userModifyInfo.userModifyInfo()
            case 5:  #userLogout()
                condition = False
                print("[System] Program Terminated")
                #CLEAR login token
            case _:
                print("Error, try again.")