FILE_SYSTEM = "file_system.txt"

def write_data():
    data = input("Enter your info: ").strip()
    with open(FILE_SYSTEM, "a") as file:  
        file.write(data + "\n")
    print("Data saved successfully!")

def read_data():
    try:
        with open(FILE_SYSTEM, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No data found!")
            else:
                print("\nYour Stored Data:")
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("No data file found yet!")

def delete_Data():
    try:
        with open(FILE_SYSTEM, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No data found!")
            return

        print("\nYour Stored Data:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")

        choice = int(input("Enter entry number to delete: "))

        if 1 <= choice <= len(lines):
            deleted = lines.pop(choice - 1)
            with open(FILE_SYSTEM, "w") as file:
                file.writelines(lines)
            print(f"Deleted entry: {deleted.strip()}")
        else:
            print("Invalid entry number!")

    except FileNotFoundError:
        print("No data file found yet!")

def clear_All_Data():
    confirm = input("Are you sure you want to delete ALL data? (yes/no): ").strip().lower()
    if confirm == "yes":
        open(FILE_SYSTEM, "w").close()  
        print("All data cleared successfully!")
    else:
        print("Operation cancelled.")

def update_Data():
    try:
        with open(FILE_SYSTEM, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No data found!")
            return

        print("\nYour Stored Data:")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")

        choice = int(input("Enter entry number to update: "))

        if 1 <= choice <= len(lines):
            new_data = input("Enter new data: ").strip()
            lines[choice - 1] = new_data + "\n"
            with open(FILE_SYSTEM, "w") as file:
                file.writelines(lines)
            print("Entry updated successfully!")
        else:
            print("Invalid entry number!")

    except FileNotFoundError:
        print("No data file found yet!")

def menu():
    while True:
        print("\n==== File Storage System ====")
        print("1. Write Data")
        print("2. Read Data")
        print("3. Delete Specific Data")
        print("4. Update Data")
        print("5. Clear All Data")
        print("6. Exit")

        choice = input("Enter number between 1 to 6: ").strip()
        if choice == "1":
            write_data()
        elif choice == "2":
            read_data()
        elif choice == "3":
            delete_Data()
        elif choice == "4":
            update_Data()
        elif choice == "5":
            clear_All_Data()
        elif choice == "6":
            print("Bye Bye")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
