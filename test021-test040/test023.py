count = 1
while count <= 3:
    print(f"This is the {count} try",f"and you have {3-count} tries left")
    Account_Name = input("Enter Account Name: ")
    Account_Password = input("Enter Account Password: ")
    if Account_Name == "admin" and Account_Password == "admin":
        print("\n")
        print("------------------------------------------------")
        print("|                                              |")
        print("|           Welcome to the system!             |")
        print("|                                              |")
        print("------------------------------------------------")
        print("\n")
        break
    else:
        print("Incorrect Account Name or Password")
        count = count + 1
        print("==============try it again !===================")
        if count == 4:
            print("\n")
            print("------------------------------------------------")
            print("|               Warning!!!                     |")
            print("| You have entered the wrong password 3 times! |")
            print("| this account is locked for 15 minute!        |")
            print("| Please contact the system administrator!     |")
            print("------------------------------------------------")
            print("\n")
            break