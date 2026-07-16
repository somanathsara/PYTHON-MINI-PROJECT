import time
import getpass
import random
import sys
NAME = "gudu"
PASSWORD = "Somanath@123"
attempt = 0
def PlaynumberGuessing_game():
    n = random.randint(1,100)
    count = 0
    while True:
            try:
                a = int(input("Guess the number here: "))
                count += 1
                if a<n:
                    print("Enter higher number please.")
                elif a>n:
                    print("Enter lower number please.")
                elif a == n:
                    print(f"You Guess {n} in {count} number of Guesss.")
            except ValueError:
                print("Please give a valid input.")
def view_profile():
    print("Name = Somanath sara")
    print("Password : Somanath@123")
    print("Profession : Engineer")
    print("Contact number : 9938773529")
    print("Email : somanathsaras@gmail.com")
def change_pasword():
    new_password = getpass.getpass("Enter new password here: ",echo_char="*")
    PASSWORD = new_password
    return PASSWORD
def Logout():
    sys.exit()
while True:
    print("==========LOGIN SYSTEM==========")
    attempt += 1
    name = input("Enter the user name here: ")
    password = getpass.getpass("Enter the password here: ",echo_char="*")
    if(name != NAME or password != PASSWORD):
        print("Invalid Credential !")
        if attempt == 3:
            for i in range(30, 0, -1):
                print(f"Try after {i} second")
                time.sleep(1)
        elif attempt == 6:
            for i in range(60, 0, -1):
                print(f"Try after {i} second")
                time.sleep(1)
        elif attempt == 7:
            for i in range(120, 0, -1):
                print(f"Try after {i} second")
                time.sleep(1)
        elif attempt == 8:
            print("Too many failed attempts.")
            print("Access Denied permanetly")
            sys.exit()       
    elif(name == NAME and password == PASSWORD):
        print("1.Play Number Guessing Game")
        print("2.View Profile")
        print("3.Change Password")
        print("4.Log Out")
        try:
            choice = input("Enter choice here(1-4): ")
            if choice == '1':
                PlaynumberGuessing_game()
            elif choice == '2':
                view_profile()
            elif choice == '3':
                PASSWORD = change_pasword()
            elif choice == '4':
                Logout()
        except ValueError:
            print("Please enter valid input: ")
           
        
        
