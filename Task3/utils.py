def rot13(text):
    """
    Applies the ROT13 encryption to the input text.

    Args:
        text (str): The input text to be encoded or decoded.

    Returns:
        str: The result of applying the ROT13 encryption to the input text.
    """

    result = ''
    for char in text:
        if char.isalpha():
            # Determine the shift value based on whether the character is lowercase or uppercase
            shift = 13 if char.islower() else -13

            # Apply ROT13 transformation to the character
            result += chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26)
                          + ord('a' if char.islower() else 'A'))
        else:
            # Preserve non-alphabetic characters
            result += char
    return result


def read_file():
    """
    Reads the contents of the 'passwd.txt' file and returns a list of lines.
    """

    with open('passwd.txt', 'r') as file:
        lines = file.readlines()
        return lines


def write_file(lines):
    """
    Writes the given list of lines to the 'passwd.txt' file.
    """

    with open('passwd.txt', 'w') as file:
        file.writelines(lines)
