import json
with open("data.json", "r")as file:
    data = json.load(file)
username = input("ENter user name: ")
password = input("Enter pasword: ")

if username in data:
    if password == data[username]["Password"]:
        print("Login succesfull")
    else:
        print("Wrong password")
else:
    print("User not found")

with open("data.json", "w") as file:
    json.dump(data, file, indent = 4)