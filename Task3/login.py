# Importing the rot13, read_file, and write_file functions
from utils import rot13, read_file
import maskpass


def log_in():
    # Reading existing user data from the file
    saved_user_data = read_file()

    username = input("User: ").lower()
    flag = False
    password = maskpass.askpass("Password: ", mask=' ').lower()
    encrypted_password = rot13(password)

    for line in saved_user_data:
        saved_username, _, saved_encrypted_password = line.strip().split(':')

        if username == saved_username and encrypted_password == saved_encrypted_password:
            flag = True
            break

    if flag:
        print("Access granted.")
    else:
        print("Access denied.")


if __name__ == "__main__":
    log_in()
