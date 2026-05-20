def print_welcome():
    print("\n")
    print("------------------------------------------------")
    print("|                                              |")
    print("|           Welcome to the system!             |")
    print("|                                              |")
    print("------------------------------------------------")
    print("\n")


def print_warning():
    print("\n")
    print("------------------------------------------------")
    print("|               Warning!!!                     |")
    print("| You have entered the wrong password 3 times! |")
    print("| This account is locked for 15 minutes!       |")
    print("| Please contact the system administrator!     |")
    print("------------------------------------------------")
    print("\n")


max_attempts = 3
for attempt in range(1, max_attempts + 1):
    print(f"This is the {attempt} try and you have {max_attempts - attempt} tries left.")
    account_name = input("Enter Account Name: ").strip()
    account_password = input("Enter Account Password: ").strip()

    if account_name == "admin" and account_password == "admin":
        print_welcome()
        break
    else:
        print("Incorrect Account Name or Password")
        print("==============try it again!===================")
else:
    # This block executes if the loop completes without a 'break'
    print_warning()