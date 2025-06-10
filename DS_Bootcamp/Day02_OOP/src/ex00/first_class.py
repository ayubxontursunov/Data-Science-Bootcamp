class Read:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    print(line, end='')
        except FileNotFoundError:
            print(f"The file {self.filename} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == '__main__':
    obj = Read("data.csv")
    obj.read_file()
