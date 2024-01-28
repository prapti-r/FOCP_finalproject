def rot13(text):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26)
                          + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result


def read_file():
    with open('passwd.txt', 'r') as file:
        lines = file.readlines()
        return lines


def write_file(lines):
    with open('passwd.txt', 'w') as file:
        file.writelines(lines)
