class Research:
    def __init__(self,filename):
        self.filename = filename

    def file_reader(self):
        with open(self.filename,'r',encoding='utf-8') as file:
            lines = file.readlines()
        return lines


if __name__ == "__main__":
    obj = Research("data.csv")
    lis = obj.file_reader()
    print(*lis, end="",sep="")
 # Remove newlines from each line and then print them
 #    print(*[line.strip() for line in lis], end="", sep="")