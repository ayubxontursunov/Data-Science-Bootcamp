import timeit

def get_data_loop(emails):
    result = []
    for email in emails:
        result.append(email)
    return result

def get_data_lc(emails):
    return [email for email in emails]

def get_data_map(emails):
    return list(map(lambda email: email, emails)) 
if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    emails *= 5  
    numbers = 90000000  


    loop_time = timeit.timeit(lambda: get_data_loop(emails), number=numbers)
    lc_time = timeit.timeit(lambda: get_data_lc(emails), number=numbers)
    map_time = timeit.timeit(lambda: get_data_map(emails), number=numbers)


    times = sorted([loop_time, lc_time, map_time])

    if times[0] == loop_time:
        print('It is better to use a loop')
    elif times[0] == lc_time:
        print('It is better to use a list comprehension')
    else:
        print('It is better to use a map')

    print(f"{times[0]} vs {times[1]} vs {times[2]}")
