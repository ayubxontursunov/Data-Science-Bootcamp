import sys


def extract_names(email_file_path):
    with open(email_file_path, 'r') as file:
        emails = file.read().splitlines()

    employees = [("Name", "Surname", "E-mail")]

    for email in emails:
        try:
            name, surname = email.split('@')[0].split('.')
            employees.append((name.capitalize(), surname.capitalize(), email))
        except ValueError:
            continue  # Skip malformed emails

    with open('employees.tsv', 'w') as file:
        for entry in employees:
            file.write('\t'.join(entry) + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <email_file_path>")
    else:
        extract_names(sys.argv[1])
