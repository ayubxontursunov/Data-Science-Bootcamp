# analytics.py
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        if has_header:
            lines = lines[1:]  # skip header

        data = []
        for line in lines:
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f"Invalid line format: {line}")
            if not all(part in ['0', '1'] for part in parts):
                raise ValueError(f"Invalid values: {line}")
            data.append([int(parts[0]), int(parts[1])])

        return data

    class Calculations:
        def counts(self, data):
            head_count = sum(pair[0] for pair in data)
            tail_count = sum(pair[1] for pair in data)
            return head_count, tail_count

        def fractions(self, heads, tails):
            total = heads + tails
            if total == 0:
                return 0.0, 0.0
            return (heads / total * 100), (tails / total * 100)

    class Analytics(Calculations):
        def predict_random(self, total):
            return [[x, 1 - x] for x in (randint(0, 1) for _ in range(total))]

        def predict_last(self, data):
            return data[-1] if data else None

        def save_file(self, data, filename, extension):
            with open(f"{filename}.{extension}", 'w') as file:
                for line in data:
                    file.write(str(line) + '\n')
