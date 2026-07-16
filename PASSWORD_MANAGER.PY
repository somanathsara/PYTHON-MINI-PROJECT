import random
import getpass,sys
import json
import string
def load_user():
    with open("users.json", "r")as file:
        data = json.load(file)
    return data
def save_user(user, mpass):
    data = load_user()
    data[user]={"Masterpassword" : mpass}
    with open("users.json", "w")as file:
        json.dump(data, file, indent = 4)
def register():
    user = input("Enter user name here: ")
    data = load_user()
    if user in data:
        print("User already exist")
    else:
        mpassword = input("Enter your master password: ")
        save_user(user, mpassword)
def login():
    global current_user
    name = input("Please enter your name here: ")
    password = input("Please enter your password here: ")
    data = load_user()
    if name in data:
        if data[name]["Masterpassword"] == password:
            print("Access granted ")
            current_user = name
        else:
            print("Access denied! You entered wrong password")
    else:
        print("User doesn't exist")
    
def load_password():
    ...
def save_password():
    global current_user
    
def add_password(current_user):
    ...
def view_password(current_user):
    ...
def search_password(current_user):
    ...
def update_password(current_user):
    ...
def delete_password(current_user):
    ...
def generate_password(current_user):
    ...
def change_master_password(current_user):
    ...
    
while True:
    print("========== PASSWORD MANAGER ==========")
    print("1.Register")
    print("2.Login")
    print("3.Exit")
    choice = input("Enter your choice here: ")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        sys.exit()
        
        
    
    