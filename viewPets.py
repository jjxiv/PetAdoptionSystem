import mainMenu,os
def availablePets():
    print("==========View Available Pets==========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Exit")
    x = int(input("Enter number: "))

    match x:
        case 1:
            pass
            print("==========Dogs==========")
            #WARNING: display dog pets from txt file
            if os.path.exists("dogsDatabase.txt"):
                f = open("dogsDatabase.txt", "r+")

                lines = f.readlines()
                lines = [line.strip('\n').strip() for line in lines]
                lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
                chunks = []
                for i in range(0, len(lines), 8):
                    chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
                    chunks.append(chunk)

                headers = ["Pet ID", "Owner ID", "Name", "Breed", "Gender", "Age", "Photo"]
                print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*headers))

                for chunk in chunks:
                    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))

                input("Press enter to continue.")
            else:
                open("dogsDatabase.txt", "x")
                input("List is empty. Press enter to continue.")

        case 2:
            pass
            print("==========Cats==========")
            # WARNING: display cat pets from txt file
            if os.path.exists("catsDatabase.txt"):
                f = open("catsDatabase.txt", "r+")

                lines = f.readlines()
                lines = [line.strip('\n').strip() for line in lines]
                lines = [line.split(':')[1].strip() if ':' in line else line for line in lines]
                chunks = []
                for i in range(0, len(lines), 8):
                    chunk = [line.split(':')[1].strip() if ':' in line else line for line in lines[i:i + 8]]
                    chunks.append(chunk)

                headers = ["Pet ID", "Owner ID", "Name", "Breed", "Gender", "Age", "Photo"]
                print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*headers))

                for chunk in chunks:
                    print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(*chunk))

                input("Press enter to continue.")
            else:
                open("catsDatabase.txt", "x")
                input("List is empty. Press enter to continue.")
        case 3:
            mainMenu.mainMenu()
            pass
        case __:
            pass