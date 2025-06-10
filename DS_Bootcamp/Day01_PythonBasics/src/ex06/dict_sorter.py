def convert():
    new_dic = dict()
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    for country,number in list_of_tuples:
        new_dic[country] = int(number)
    return new_dic

def sort_key(item):
    country, number = item
    return (-number,country)

def sort_dict(new_dic):
    sorted_countries = sorted(new_dic.items(),key=sort_key)

    for country, _ in sorted_countries:
        print(country)



if __name__ == '__main__':
    res = convert()
    sort_dict(res)