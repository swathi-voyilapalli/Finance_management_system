
from Databse import init_db,register_user,authenticate_user
from home import finance_home
def main():
    init_db()
    while True:
        print("WELCOME TO FINANCE SYSTEM\n\n")
        choice = input("1. Register\n2. Login\n\nChoose an option: ")
        if choice == '1':
            username = input("\nEnter username: ")
            password = input("\nEnter password: ")
            register_user(username, password)
            print("\nRegistration successful.")
        elif choice == '2':
            username = input("\nEnter username: ")
            password = input("\nEnter password: ")
            if authenticate_user(username, password):
                print("\nLogin successful.\n\n")
                finance_home(username)
                break
            else:
                print("Invalid credentials.\n\n")

if __name__ == "__main__":
    main()
