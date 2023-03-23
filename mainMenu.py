"""
    File name:      mainMenu.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the main menu for Pet Adoption System.
                    It consists of different functions from different python
                    files.
    Date:
"""


# Imported python files
import adminMainMenu
import viewPets, userMainMenu, os


"""
    Method name:    register()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the registration for every user
                    that will be using the Pet Adoption System.
"""
def register():
    print("============Register=============")
    if os.path.exists("userDatabase.txt"):
        print("[System] Retrieving existing files")
        f = open("userDatabase.txt","r+")
        userID = [] # This variable stores the user id's
        text = f.readline()
        ctr = 0

        # Gets the user id for every read line from text file
        while text:
            if ctr%7==0:
                userID.append(text)
            text = f.readline()
            ctr+=1

        # Gets the last greatest ID value and automatically generate new ID
        print("")
        idNum = []
        for i in userID:
            temp = int(i.replace("UserID:", "").strip())
            idNum.append(temp)
        lastID = max(idNum)
        lastID = str(int(lastID)+1)
        f.write("\n")
        f.write("UserID:"+lastID+"\n")


    else:
        # If the file does not exist, create new file and set UserID to 1 as start
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

    # Display information from user input
    print("=======================================")
    print("Registration information:")
    print("Username:",userName)
    print("Password:",password)
    print("Name:",name)
    print("Email Address:",emailAddress)
    print("Birthday:",birthday)
    print("=======================================")

    # User will input if the registration should be saved
    confirmq = input("Save registration? [Y/N]")
    match confirmq:
        case "y" | "Y":
            f.write("Username:" + userName + "\n")
            f.write("Password:" + password + "\n")
            f.write("Name:" + name + "\n")
            f.write("EmailAddress:" + emailAddress + "\n")
            f.write("Bday:" + birthday + "\n")
            print("[System] Registration success...")
        case "n" | "N":
            print("[System] Registration cancelled...")
            pass
        case _:
            print("[System] Invalid input, please try again...")
    input("Press Enter to continue...")
    f.close()


"""
    Method name:    mainMenu()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains the main menu for the user to 
                    navigate over the Pet Adoption System.
"""
def mainMenu():
    condition = True
    # Loop the main menu until condition is set to False
    while condition:
        print("==========Pet Adoption System==========")
        print("[1] Register")
        print("[2] User Login")
        print("[3] Admin Login")
        print("[4] View Available Pets")
        print("[5] Exit")
        print("=======================================")
        choice = int(input("Enter a number: "))

        match choice:
            case 1:
                # Register Function
                # !!!WARNING!!!
                # Note: Delete userRegister.py file in github master repo
                # If done, delete this comment and the comment above
                # Regitser user
                register()
            case 2:
                # User Login
                userMainMenu.login()
            case 3:
                # Admin Login
                adminMainMenu.login()
            case 4:
                # View Available Pets
                viewPets.availablePets()
            case 5:
                # Temrinates Pet Adoption System
                condition = False
                print("[System] Program Terminated...")
            case _:
                print("[System] Invalid input, please try again...")


# Main method calling mainMenu()
if __name__ == "__main__":
    mainMenu()

