import sys


def find_name(email):
    with open('employees.tsv', 'r') as file:
        lines = file.readlines()[1:]  # Skip header

    for line in lines:
        name, surname, stored_email = line.strip().split('\t')
        if stored_email == email:
            return name
    return None


def generate_letter(email):
    name = find_name(email)
    if name:
        print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you.\n"
              "That's a precondition for the professionals that our company hires.")
    else:
        print("Email not found in the database.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python letter_starter.py <email>")
    else:
        generate_letter(sys.argv[1])
