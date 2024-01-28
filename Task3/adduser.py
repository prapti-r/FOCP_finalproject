# Importing the rot13, read_file, and write_file functions from utils module
from utils import rot13, read_file, write_file


def add_user():
    """
    Allows a user to add new user.
    Adds a new user by taking input for username, real name, and password.
    Encrypts the password using ROT13 and stores the user data in the 'passwd.txt' file.
    """

    # Reading existing user data from the file
    saved_user_data = read_file()

    while True:
        username = input("Enter new username: ").lower()
        flag = False

        # Checking if the username already exists
        for line in saved_user_data:
            if username == line.strip().split(':')[0]:
                flag = True
                break

        if flag:
            print("Cannot add. Most likely username already exists.")

        else:
            real_name = input("Enter real name:")
            password = input("Enter password:").lower()

            # Encrypting the password using rot13
            encrypted_password = rot13(password)

            new_data = f"{username}:{real_name}:{encrypted_password}\n"
            saved_user_data.append(new_data)

            # Writing the user data in the file
            write_file(saved_user_data)
            print("User Created.")
            break


# Calling the add_user function
if __name__ == "__main__":
    add_user()
