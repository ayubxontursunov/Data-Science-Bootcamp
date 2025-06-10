import sys

def process_input():
    if len(sys.argv) == 4:
        task = sys.argv[1]
        msg = sys.argv[2]
        try:
            shift = int(sys.argv[3])
        except ValueError:
            raise Exception("The shift value must be an integer.")
        return task, msg, shift
    else:
        raise Exception("Incorrect number of arguments. Usage: python3 caesar.py <encode/decode> <message> <shift>")

def encode(msg, shift):
    result = ""
    for char in msg:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def decode(msg, shift):
    result = ""
    for char in msg:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char.lower()) - ord('a') - shift_amount) % 26) + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result

def check_for_cyrillic(msg):
    for char in msg:
        if 'а' <= char <= 'я' or 'А' <= char <= 'Я':
            raise Exception("The script does not support your language yet.")

if __name__ == "__main__":
    try:
        task, msg, shift = process_input()
        check_for_cyrillic(msg)  # Check for Cyrillic symbols in the message

        if task.lower() == 'decode':
            print(decode(msg, shift))
        elif task.lower() == 'encode':
            print(encode(msg, shift))
        else:
            raise Exception("Invalid task. Use 'encode' or 'decode'.")
    except Exception as e:
        print(f"Error: {e}")
