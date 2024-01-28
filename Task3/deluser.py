# Importing the rot13, read_file, and write_file functions from utils module
from utils import rot13, read_file, write_file
import maskpass


def del_user():
    """
    Allows a user to delete a user.
    Deletes a user by taking input for username and password. 
    The password is masked using the 'maskpass' module and encrypted using ROT13.
    Updates the 'passwd.txt' file with the modified user data.
    """

    # Reading existing user data from the file
    saved_user_data = read_file()

    username = input("Enter username: ").lower()
    flag = False

    password = maskpass.askpass("Password: ", mask=' ').lower()
    encrypted_password = rot13(password)

    # Iterate through the lines to find and delete the user
    new_lines = []
    for line in saved_user_data:
        saved_username, _, saved_password = line.strip().split(':')
        if username == saved_username and encrypted_password == saved_password:
            flag = True
        else:
            new_lines.append(line)

    if flag:
        write_file(new_lines)
        print("User Deleted.")
    else:
        print("Username and password do not match.")


# Calling the del_user function
if __name__ == "__main__":
    del_user()
