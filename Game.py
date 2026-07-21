import time
import random
import getpass
n = random.randint(1,100)
PASSWORD = "Somanath@123"
attempt = 0
count = 0
while True:
    password = getpass.getpass("Enter  the correct password to play the game :", echo_char= "*")
    if(password == PASSWORD):
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
                    exit()
            except ValueError:
                print("Please give a valid input.")
    else:
        print("Incorrect password ! Try again")
        attempt += 1
        if attempt == 3:
          print("Too many attempts wait 30 second.")
          for i in range(30, 0, -1):
           print(f"Try again in {i} second")
           time.sleep(1)
        elif attempt == 6:
          print("Too many attempts wait 60 second.")
          for i in range(60, 0, -1):
           print(f"Try again in {i} second")
           time.sleep(1)
        elif attempt == 7:
          print("Last attempt but able to see after 2 min")
          for i in range(120, 0, -1):
             print(f"Try again in {i} second")
             time.sleep(1)
        elif attempt == 8:
          print("Access Denied")
          break
    