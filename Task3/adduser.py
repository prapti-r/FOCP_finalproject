# Importing the rot13, read_file, and write_file functions
from utils import rot13, read_file, write_file


def add_user():
    # Reading existing user data from the file
    saved_user_data = read_file()

    while True:
        username = input("Enter new username: ").lower()
        flag = False

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

            write_file(saved_user_data)
            print("User Created.")
            break


if __name__ == "__main__":
    add_user()
