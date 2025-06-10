import sys


class Research:
    def __init__(self, filename):
        self.filename = filename  # Store the file path

    def file_reader(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()


                header = lines[0].strip()
                if len(header.split(',')) != 2:
                    raise ValueError("Header does not contain exactly two values separated by a comma")

                # Check the lines for correct structure: either "0,1" or "1,0"
                for line in lines[1:]:
                    parts = line.strip().split(',')
                    if len(parts) != 2 or not (parts[0] in ['0', '1'] and parts[1] in ['0', '1']):
                        raise ValueError(f"Invalid line format: {line.strip()}")

                return lines

        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
            raise
        except ValueError as e:
            print(f"Error: {e}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py <path_to_file>")
        sys.exit(1)


    file_path = sys.argv[1]

    try:

        obj = Research(file_path)


        lis = obj.file_reader()
        for line in lis:
            print(line, end='')
    except Exception as e:
        print(f"Error reading file: {e}")
