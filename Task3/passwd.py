# Importing the rot13, read_file, and write_file functions from utils module
from utils import rot13, read_file, write_file
import maskpass


def change_password():
    """
    Allows a user to change their password. 
    Asks for the current password and checks it against saved data.
    If the current password is correct, the user is ask for a new password.
    The new password is encrypted using ROT13 and saved back to the 'passwd.txt' file.
    """

    # Reading existing user data from the file
    saved_user_data = read_file()

    username = input("User: ").lower()
    updated_user_data = []  # New list to store the updated user data

    flag = False

    for line in saved_user_data:
        saved_username, saved_real_name, saved_encrypted_password = line.strip().split(':')

        if username == saved_username:
            flag = True
            password = maskpass.askpass("Current Password: ", mask=' ').lower()
            encrypted_password = rot13(password)

            if encrypted_password != saved_encrypted_password:
                print("Incorrect current password.")
                return  # Exit the function if the current password is incorrect

            new_password = maskpass.askpass("New Password: ", mask=' ').lower()
            confirm_password = maskpass.askpass("Confirm: ", mask=' ').lower()

            if new_password == confirm_password:
                # Append the user data with the new password to the new list
                updated_user_data.append(
                    f"{saved_username}:{saved_real_name}:{rot13(new_password)}\n")
                print("Password changed.")
            else:
                print("New passwords do not match.")
        else:
            # Append unchanged lines to the new list
            updated_user_data.append(line)

    if not flag:
        print("Username not found.")

    # Write the  data back to the file
    write_file(updated_user_data)


# Calling the change_password function
if __name__ == "__main__":
    change_password()
