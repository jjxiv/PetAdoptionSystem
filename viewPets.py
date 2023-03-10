import mainMenu
def availablePets():
    print("==========View Available Pets==========")
    print("[1] Dogs")
    print("[2] Cats")
    print("[3] Cats")
    x = int(input("Enter number: "))

    match x:
        case 1:
            pass
            print("==========Dogs==========")
            #WARNING: display dog pets from txt file
        case 2:
            pass
            print("==========Cats==========")
            # WARNING: display cat pets from txt file
        case 3:
            mainMenu.mainMenu()
            pass
        case __:
            pass