from functools import reduce
import timeit
import sys




def with_loop(n):
    sum = 0
    for i in range(n):
        sum = sum + i*i
    return sum

def with_reduce(n):
    return reduce(lambda sum,i: sum + i*i,range(1,n+1))

def time_taken():
    if len(sys.argv) != 4:
        exit(1)
    
    method = sys.argv[1]
    iterations = int(sys.argv[2])
    num_cal=int(sys.argv[3])
    if method =="loop":
        time_spent = timeit.timeit(lambda : with_loop(num_cal),number=iterations)
    elif method =="reduce":
        time_spent = timeit.timeit(lambda : with_reduce(num_cal),number=iterations)
    else:
        exit(1)
    return time_spent

if __name__ == '__main__':
    time_function = time_taken()
    print(time_function)