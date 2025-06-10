import timeit

def get_data_loop(emails):
    result = []
    for email in emails:
        result.append(email)

    return result


def get_data_lc(emails):
    return [email for email in emails]


if __name__ == '__main__':
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com','anna@live.com', 'philipp@gmail.com']
    emails = 5 * emails
    numbers = 90000000
    # get_data_loop(emails)
    # get_data_lc(emails)
    time_loop = timeit.timeit(lambda: get_data_loop(emails),number = numbers)
    time_lc = timeit.timeit(lambda: get_data_lc(emails),number = numbers)
    if time_loop >= time_lc:
        print('It is better to use a list comprehension')
    else:
        print('It is better to use a loop')

    times = sorted([time_loop, time_lc])
    print(f"{times[0]} vs {times[1]}")
