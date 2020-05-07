# Caesear exercise: Implement a program that encrypts messages using Caesar’s cipher,

def encode_char(char: str, key:int) -> str:
    assert len(char) == 1
    if not char.isalpha():
        return char

    # Convert char to ascii number using ord()
    ascii_code:int = ord(char)
    # Check for uppercase (starts at 65 on ASCII chart)
    if ascii_code < 97:
        ascii_table_offset = 65
    # Check for lowercase (starts at 97 on ASCII chart)
    else:
        ascii_table_offset = 97

    # We can't work directly on the ascii numbers because they don't start with one and end on 25, so we need to
    # first convert the ascii_code number to our own alpha_code so that we can run modulo on it (for handling Z).
    alpha_code = ascii_code - ascii_table_offset

    # Once we have the code in a 0-25 range, we can safely use modulo, wrapping a z+1 back to a.
    alpha_code = (alpha_code + key) % 26

    # Now, we need to return the character, but need to convert back to the ascii_code for the letter by adding
    # the offset back to it.
    ascii_code = alpha_code + ascii_table_offset

    # Convert the updated ascii_code back into the right letter using chr() and return it.
    char = chr(ascii_code)
    return char

# Add each encoded string to new_string
def encode(string: str, key: int) -> str:
    new_string = ''
    for letter in string:
        new_string += encode_char(letter, key)
    return new_string


# Test to ensure functions are working as they should
assert ' ' == encode_char(' ', 1)
assert 'L' == encode_char('K', 1)
assert 'l' == encode_char('k', 1)
assert ' ' == encode(' ', 1)
assert 'L' == encode('K', 1) , "output was : " + encode('K', 1)


if __name__ ==  '__main__':
    number = input('Enter a number: ')

    if number.isdigit():
        print('Success')
    else:
        print('1: Error. Please enter a number.')

    key = int(number)

    string = input('Enter a word or phrase: ')
    encoded = encode(string, key)
    print(encoded)