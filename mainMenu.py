"""
    File name:
    Authors:
    Description:
    Date:
    Email:
"""
import adminMainMenu
import viewPets, userMainMenu, os

def register():
    print("============Register=============")
    if os.path.exists("userDatabase.txt"):
        print("[System] Retrieving existing files")
        f = open("userDatabase.txt","r+")
        userID = []
        text = f.readline()
        ctr = 0

        while text:
            if ctr%7==0:
                userID.append(text)
            text = f.readline()
            ctr+=1

        print("UserID values:",userID)
        print("")
        lastID = userID[-1]
        lastID = lastID.replace("UserID:","")
        lastID = str(int(lastID)+1)
        f.write("\n")
        f.write("UserID:"+lastID+"\n")

    else:
        print("[System] Creating a new file")
        f = open("userDatabase.txt", "w")
        f.write("UserID:"+"1\n")
        pass

    userName = str(input("Enter username: "))
    password = str(input("Enter password: "))
    name = str(input("Enter name: "))
    emailAddress = str(input("Enter Email Address: "))
    birthday = str(input("Enter birthday: "))
    print()

    print("Registration information:")
    print("Username:",userName)
    print("Password:",password)
    print("Name:",name)
    print("Email Address:",emailAddress)
    print("Birthday:",birthday)
    print("=======================================")
    input("Press Enter to continue...")



    f.write("Username:"+userName+"\n")
    f.write("Password:"+password+"\n")
    f.write("Name:"+name+"\n")
    f.write("EmailAddress:"+emailAddress+"\n")
    f.write("Bday:"+birthday+"\n")

    f.close()
    #WARNING: insert codes here to save name to database


def mainMenu():
    condition = True
    #WARNING: insert validation here
    while condition:
        print("==========Pet Adoption System==========")
        print("[1] Register")
        print("[2] User Login")
        print("[3] Admin Login")
        print("[4] View Available Pets")
        print("[5] Exit")
        print("=======================================")
        mm = int(input("Enter a number: "))
        match mm:
            case 1:
                # Register Function
                register()
            case 2:
                #User Login
                userMainMenu.login()
            case 3:
                #Admin Login
                adminMainMenu.adminMainMenu()
            case 4:
                viewPets.availablePets()
                #View Available Pets
            case 5:
                condition = False
                print("[System] Program Terminated")
            case _:
                print("Error, try again.")


if __name__ == "__main__":
    mainMenu()

