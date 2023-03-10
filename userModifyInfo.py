

def userModifyInfo():

    #retrieve user information

    userName = str(input("Enter new username:"))
    password = str(input("Enter new password:"))
    name = str(input("Enter name:"))
    emailAddress = str(input("Enter email address:"))
    birthday = str(input("Enter Birthday:"))

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