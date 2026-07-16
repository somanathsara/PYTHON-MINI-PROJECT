import random
import sys
import bcrypt,pyperclip
from getpass import getpass
import json
import string
def load_user():
    with open("users.json", "r")as file:
        data = json.load(file)
    return data
def load_data():
    try:
        with open("data.json","r")as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def save_user(user, hashed):
    data = load_user()
    data[user]={"Masterpassword" : hashed}
    with open("users.json", "w")as file:
        json.dump(data, file, indent = 4)
def register():
    user = input("Enter user name here: ")
    data = load_user()
    if user in data:
        print("User already exist")
    else:
        mpassword = getpass("Enter your master password: ", echo_char="*")
        hashed = bcrypt.hashpw(mpassword.encode(),bcrypt.gensalt()).decode()
        save_user(user, hashed)
def login():
    global current_user
    name = input("Please enter your name here: ")
    password = getpass("Please enter your password here: ",echo_char="*")
    data = load_user()
    if name not in data:
        print("-"*25)
        print("User not found")
        print("-"*25)
        return
    stored_hash = data[name]["Masterpassword"] 
    if bcrypt.checkpw(password.encode(),stored_hash.encode()):
            print("-"*30)
            print("Access granted ")
            print("-"*30)
            current_user = name
            while True:
                print("1.Add password"," "*20,"2.View password")
                print("3.Search"," "*26,"4.Update")
                print("5.Delete"," "*26,"6.Generate password.")
                print("7.Change master password"," "*10,"8.Logout")
                choice = input("Enter your choice here :")
                if choice == '1':
                    save_password()
                elif choice == '2':
                    view_password(current_user)
                elif choice == '3':
                    search_password(current_user)
                elif choice == '4':
                    update_password(current_user)
                elif choice == '5':
                    delete_password(current_user)
                elif choice == '6':
                    generate_password(current_user)
                elif choice == '7':
                    change_master_password(current_user)
                elif choice == '8':
                    break    
                else:
                    print("-"*25)
                    print("Please input valid choice!")
                    print("-"*25)
    else:
            print("-"*35)
            print("Access denied! You entered wrong password")
            print("-"*35)
            return

def save_password():
    global current_user
    website = input("Enter the name of your website: ")
    user = input(f"Enter the user name for {website}: ")
    password = getpass("Enter the password for the website: ",echo_char="*")
    data = load_data()
    if current_user not in data:
        data[current_user]= {}
    data[current_user][website] = {"username":user, "password":password}
    with open ("data.json", "w") as file:
        json.dump(data, file, indent = 4)       
def view_password(current_user):
    data = load_data()
    if current_user not in data:
        print("-"*30)
        print("User not found")
        print("-"*30)
        return 
    password = data[current_user]
    if not password:
        print("-"*30)
        print("No password yet")
        print("-"*30)
        return 
    for website, details in password.items():
        print("-"*40)
        print(f"Website : {website}")
        print(f"username : {details['username']}")
        print(f"password : {details['password']}")
def search_password(current_user):
    data = load_data()
    if current_user not in data:
        print("-"*30)
        print("User not found")
        print("-"*30)
        return
    Website = input("Enter website name here: ")
    if Website in data[current_user]:
        print("\nPassword found")
        print(f"Website : {Website}")
        print(f"Username : {data[current_user][Website]['username']}")
        print(f"Password : {data[current_user][Website]['password']}")
    else:
        print("-"*30)
        print("Websit not found")
        print("-"*30)
def update_password(current_user):
    data = load_data()
    website = input("Enter your website name which password wants to change: ")
    newpassword = getpass("Please enter your new password:",echo_char="*")
    newuser = input("Do you want to change user name(y/n)")
    if current_user not in data:
        print("-"*30)
        print("User not found")
        print("-"*30)
        return
    if website not in data[current_user]:
        print("-"*30)
        print("Wesite not found")
        print("-"*30)
        return
    if newuser.lower() == 'y':
        newname = input("Enter new name here:")
        data[current_user][website]['username'] = newname
    data[current_user][website]['password'] = newpassword
    with open ("data.json", "w")as file:
        json.dump(data, file, indent = 4)
    print("-"*30)
    print("Updated succesfully")
    print("-"*30)
def delete_password(current_user):
    data = load_data()
    if current_user not in data:
        print("-"*30)
        print("User not found")
        print("-"*30)
        return
    website = input("Enter the website name which password wants to delete: ")
    if website not in data[current_user]:
        print("-"*35)
        print("Website not found.")
        print("-"*35)
        return 
    del data[current_user][website]
    with open ("data.json", "w")as file:
        json.dump(data, file, indent = 4)
    print("-"*30)
    print("Deleted succesfully") 
    print("-"*30)
def generate_password(current_user):
    data = load_data()
    if current_user not in data:
        print("User not found") 
    length = int(input("Please enter the length of the password(must be greater than 12): "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password += random.choice(characters)
    print(f"Password : {password}")
    choice = input("Do you want to save this paswword(y/n): ")
    if choice.lower() == 'y':
        web = input("Enter your website name please: ")
        username = input("Enter your username please: ")
        data[current_user][web] = {"username": username, "password":password}
        with open("data.json", "w")as file:
            json.dump(data, file, indet = 4)
        print("-"*40)
        print("Password generated & saved succesfully.")
        print("-"*40)

    else:
        print("-"*25)
        print("Password save failed!")
        print("-"*25)
def change_master_password(current_user):
    data = load_user()
    if current_user not in data:
        print("-"*30)
        print("User not found")
        print("-"*30)
    mpass = getpass("Enter new master password: ",echo_char="*")
    choice = input("Do you want to change your master password(y/n): ")
    if choice.lower() == 'y':
        data[current_user] = {"Massterpassword":mpass}
        with open("users.json", "w") as file:
            json.dump(data, file, indent = 4)
        print("-"*30)
        print("Change Master password succesfull")
        print("-"*30)
    else:
        print("Masterpassword changing Aborted!")
while True:
    print("========== PASSWORD MANAGER ==========")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    try:    
        choice = input("Enter your choice here: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            sys.exit()
        else:
            print("Invalid choice ! Please Enter between (1,3):")
    except ValueError:
        print("Please Enter valid option !")
        
        
    
    