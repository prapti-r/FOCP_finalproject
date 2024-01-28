# Importing the rot13, read_file, and write_file functions from utils module
from utils import rot13, read_file
import maskpass


def log_in():
    """ 
    Allows a user to change log in.
    Asks for a username and a password, then checks against the saved user data.
    Access is granted if the provided username and password match any saved credentials.
    """

    # Reading existing user data from the file
    saved_user_data = read_file()

    username = input("User: ").lower()
    flag = False

    password = maskpass.askpass("Password: ", mask=' ').lower()
    encrypted_password = rot13(password)

    # Iterate through the lines to find a matching user
    for line in saved_user_data:
        saved_username, _, saved_encrypted_password = line.strip().split(':')

        if username == saved_username and encrypted_password == saved_encrypted_password:
            flag = True
            break

    if flag:
        print("Access granted.")
    else:
        print("Access denied.")


# Calling the log_in function
if __name__ == "__main__":
    log_in()
