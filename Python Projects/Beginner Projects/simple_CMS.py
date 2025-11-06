CMS_FILE = "CMS.txt"

def add_Content():
    title = input("Enter Title: ").strip()
    body = input("Enter Body: ").strip()

    with open(CMS_FILE, "a") as file:   
        file.write("Title: " + title + "\n")
        file.write("Body: " + body + "\n")
        file.write("-" * 30 + "\n")   # separator for readability

    print("Content Added Successfully!")


def view_Content():
    try:
        with open(CMS_FILE, "r") as file:
            lines = file.readlines()

            if not lines:
                print("No Content Found!")
                return

            print("\n===== Stored Content =====")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No content file found yet.")


def menu():
    while True:
        print("\n===== Simple CMS =====")
        print("1. Add Content")
        print("2. View Content")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_Content()
        elif choice == "2":
            view_Content()
        elif choice == "3":
            print("Thank you for using Simple CMS. Bye Bye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
