import timeit
import random
from collections import Counter

def list_to_dic(nums):
    count_dict = {i: 0 for i in range(1,101)}
    for num in nums:
        if 0 < num <=100:
            count_dict[num] += 1
    return count_dict


def top_10_common(nums):
    count_dict = {}
    for num in nums:
        # converting to dict
        count_dict[num] = count_dict.get(num, 0) + 1

    # Sort the dictionary by count (values), descending, and take the top 10
    top_10 = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:10]

    return dict(top_10)

def with_counter(nums):
    my_dict = Counter(nums)
    return my_dict

def top_10_common_counter(nums):
    my_dict = Counter(nums)
    top_10_common = my_dict.most_common(10)
    return top_10_common_counter

if __name__ == '__main__':
    my_random_list = [random.randint(1,100) for i in range(10000000)]
    random_dic = list_to_dic(my_random_list)
    my_function = timeit.timeit(lambda: list_to_dic(my_random_list),number=1)
    my_top = timeit.timeit(lambda:top_10_common(my_random_list),number=1)
    counter = timeit.timeit(lambda: with_counter(my_random_list),number=1)
    counter_top = timeit.timeit(lambda: top_10_common_counter(my_random_list),number=1)

    print(f'my function: {my_function}')
    print(f'Counter: {counter}')
    print(f'my top: {my_top}')
    print(f"Counter's top: {counter_top}")
