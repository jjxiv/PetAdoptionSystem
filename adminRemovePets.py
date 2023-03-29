"""
    File name:      adminRemovePets.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the operations for removing a pet
                    through admin privileges.
"""


# Imported python library
import os


"""
    Method name:    adminRemovePets()
    Parameters:     none
    Return Type:    none
    Description:    A method that contains removing a pet through 
                    admin privileges.
"""
def adminRemovePets():
    try:
        dogsDB = "dogsDatabase.txt"
        catsDB = "catsDatabase.txt"
        valid = False

        print("============Remove Pets=============")
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
                print("[System] Invalid input, please try again...")

        if valid == True:
            if os.path.exists(petsDB):
                petIDnumber = str(input("Input the Pet ID to remove:"))
                pid = "PetID:" + petIDnumber + "\n"

                with open(petsDB, "r") as f:
                    lines = f.readlines()

                if pid in lines:
                    num = lines.index(pid)
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
                        print("[System]",pid.strip(), "has been deleted\n")
                else:
                    print("[System] \"", pid.strip(), "\" does not exist.\n")
            else:
                print("[System] There is no existing pet database\n")
        else:
            print("[System] Returning to menu")
    except:
        input("Invalid input. Please try again.")


