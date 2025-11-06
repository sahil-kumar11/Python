def login():
    input_username = input("Enter Username: ")
    input_password = input("Enter Password: ")

    found = False

    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data:
                Username, password = data.split("|")
                if Username == input_username and password == input_password:
                    found = True
                    break  

    if found:
        print("Login Successful.")
    else:
        print("Invalid credentials")


def register():
    Account_name = input("Enter Username: ")
    Account_password = input("Enter Password: ")

    found = False

    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data:
                Username, password = data.split("|")
                if Username == Account_name:
                    found = True
                    break  

    if found:
        print("User already exists.")
    else:
        with open('password.txt', 'a') as f:
            f.write(Account_name + "|" + Account_password + "\n")
        print("User added successfully.")

while True:
    Answer = input("Would you like to register,login or exit for register type 1 , for login type 2 "
               "and for exit type 3? ")
    if Answer == "1":
        register()
    elif Answer == "2":
        login()
    elif Answer == "3":
        quit()
    else:
        print("Invalid input.")