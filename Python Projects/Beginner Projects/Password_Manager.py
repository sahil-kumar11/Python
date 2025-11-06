from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#
# write_key()



def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data:
                user, passw = data.split("|")
                print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())


def add():
    Account_name = input("What is your account name? ")
    Account_password = input("What is your account password? ")

    with open ('password.txt', 'a') as f:
        f.write(Account_name + "|" + fer.encrypt(Account_password.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add new password or view existing one (add/view) or quit, for quit type q? ").lower()
    if mode == "q":
        break

    
    if mode == "view":
        view()

    
    if mode == "add":
        add()


    else : 
        print("Inavlid input")
        continue
