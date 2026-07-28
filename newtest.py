import bcrypt
from getpass import getpass
password = getpass("Enter your password here: ", echo_char="*")
print(password)
password_bytes = password.encode('utf - 8')
hashed_password = bcrypt.hashpw(
    password_bytes, bcrypt.gensalt()
)
hashed = hashed_password.decode('utf - 8')
print(hashed_password.decode('utf - 8'))
newpass = input("Enter new password here: ")
if bcrypt.checkpw(newpass.encode(), hashed.encode()):
    print("Welcome")
else:
    print("Wrong password")