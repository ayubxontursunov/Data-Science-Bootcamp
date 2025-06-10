import sys
import time
import resource
import os

def read_all_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def main():
    if len(sys.argv) != 2:
        print("Usage: ./ordinary.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Convert to absolute path if necessary
    if not os.path.isabs(file_path):
        file_path = os.path.join("/home/simmonsc/goinfre/ml-25m", file_path)

    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    start_time = time.time()

    lines = read_all_lines(file_path)
    for _ in lines:
        pass  # Just iterate through all lines

    end_time = time.time()

    # Resource usage
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory = usage.ru_maxrss / 1024 / 1024  # Convert KB -> GB
    total_time = usage.ru_utime + usage.ru_stime  # User + System time

    print(f"Peak Memory Usage = {peak_memory:.3f} GB")
    print(f"User Mode Time + System Mode Time = {total_time:.3f}s")

if __name__ == "__main__":
    main()
