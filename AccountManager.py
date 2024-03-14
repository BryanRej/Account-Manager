import hashlib 
import getpass

password_manager = {}

def create_user():
   username = input("Please enter a username: ")
   password = getpass.getpass("Please Enter a password: ")
   hashed_password = hashlib.sha256(password.encode()).hexdigest()
   password_manager[username] = hashed_password
   print(f"User {username} created successfully!")

def user_login():
  username = input("Please enter your username: ")
  password = getpass.getpass("Please enter your password: ")
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  if username in password_manager.keys() and password_manager[username] == hashed_password:
    print(f"Welcome {username}!")
  else:
    print("Invalid username or password.")
    
def main():
  while True:
    print("Welcome to the Account Manager!")
    print("1. Create User")
    print("2. Login")
    print("3. Exit")
    choice = input("Please enter your choice: ")
    if choice == "1":
      create_user()
    elif choice == "2":
      user_login()
    elif choice == "3":
      break
    else:
      print("Invalid choice. Please try again.")
  
if __name__ == "__main__":
  main()