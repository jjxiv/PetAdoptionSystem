"""
    File name:      mainMenu.py
    Authors:        Jericho John Almoro,
                    Rico Ray Alido
    Description:    The file contains the owned pet display for Pet
                    Adoption System.It consists of different functions
                    from different python files.
    Date:
"""


import os
import userMainMenu

def userDisplayOwned(userID):
    parts = userID.split(":")
    userID = int(parts[1])

    headers = ["Pet ID", "Owner ID", "Name", "Breed", "Gender", "Age", "Photo"]
    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*headers))

    #retrieve dogs owned by user
    if os.path.exists("dogsDatabase.txt"):
        f = open("dogsDatabase.txt", "r")

        lines = f.readlines()
        lines = [line.strip('\n').strip() for line in lines]
        lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
        chunks = []
        for i in range(0, len(lines), 8):
            chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
            if chunk[1] == str(userID):
                chunks.append(chunk)

        if len(chunks) == 0:
            print("No pets owned by this user.")
        else:
            for chunk in chunks:
                print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))

    else:
        open("dogsDatabase.txt", "x")

    #retrieve cats owned by user
    if os.path.exists("catsDatabase.txt"):
        f = open("catsDatabase.txt", "r")

        lines = f.readlines()
        lines = [line.strip('\n').strip() for line in lines]
        lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
        chunks = []
        for i in range(0, len(lines), 8):
            chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
            if chunk[1] == str(userID):
                chunks.append(chunk)

        if len(chunks) == 0:
            print("No pets owned by this user.")
        else:
            for chunk in chunks:
                print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))
    else:
        open("catsDatabase.txt", "x")

    input("Press enter to continue.")