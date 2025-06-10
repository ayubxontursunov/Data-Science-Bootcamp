def data_types():

    intt = 2
    string = "esese"
    fl = 2.2
    boole = True
    lis = [1, 2, 3, 4, 5]
    dic = {2: "e", 3: "r "}
    tuple1 = (3, 2, 3, 4)
    sets = {2, 3, 4, 5}


    types_list = [type(intt).__name__, type(string).__name__, type(fl).__name__, type(boole).__name__, type(lis).__name__, type(dic).__name__, type(tuple1).__name__, type(sets).__name__]
    print(types_list)


if __name__ == '__main__':
    data_types()
