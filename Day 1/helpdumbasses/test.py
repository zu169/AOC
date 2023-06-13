def checkIfUnique(username):
    print(username)

def signup():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    confirm = input("Confirm Password: ")

    if confirm == password:
        store = open("credentials.txt", "w")
        store.write(username + " " + password)
        store.close()
        print("You have registered successfully: ")
    else: 
        print("Passwords don't match")

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    passed = False

    store = open("credentials.txt", "r")
    check = store.readlines()
    for line in check:
        credential = []
        credential = line.split(" ")
        if credential[0] == username:
            if credential[1] == password:
                passed = True
                break
    if passed == True:
        print("Login Successful")
    else: 
        print("Login Failed")

def main():
    answer = 0
    while answer != 3:
        print("**Login System!**")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        answer = int(input("Enter your choice: (1,2,3)\n"))
        if answer == 1:
            signup()
        elif answer == 2:
            login()
        elif answer == 3:
            break
        else:
            print("Wrong Choice!")

main()