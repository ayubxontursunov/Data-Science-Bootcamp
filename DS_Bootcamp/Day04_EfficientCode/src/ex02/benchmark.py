import timeit
import sys

def get_data_loop(emails):
    result = []
    for email in emails:
        result.append(email)

    return result


def get_data_lc(emails):
    return [email for email in emails]


def get_data_map(emails):
    return list(map(lambda email: email, emails))

def get_data_filter(emails):
    return list(filter(lambda email: email, emails))

def input():
    if len(sys.argv) != 3:
        print("Usage: , benchpark.py <method> <iteration>")
        sys.exit(1)
    method = sys.argv[1]
    iterations = int(sys.argv[2])
    time = float()
    if method == "loop":
        time = timeit.timeit(lambda: get_data_loop(emails),number = iterations)
    elif method == "list_comprehension":
        time = timeit.timeit(lambda: get_data_lc(emails),number = iterations)
    elif method == "map":
        time = timeit.timeit(lambda: get_data_map(emails), number = iterations)
    elif method == "filter":
        time = timeit.timeit(lambda: get_data_filter(emails),number=iterations)
    else:
        print(f"Unknown method: {method}")
        exit(1)

    return time

if __name__ == '__main__':

    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com','anna@live.com', 'philipp@gmail.com']
    emails = 5 * emails

    time_taken = input()


    print(time_taken)
