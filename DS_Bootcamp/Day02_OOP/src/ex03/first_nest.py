import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise FileNotFoundError(f"File '{self.path}' does not exist.")

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

# --- Main Execution ---

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 first_nest.py <path_to_csv_file>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    try:
        research = Research(path_to_file)
        data = research.file_reader(has_header=True)
        print(data)

        calculations = research.Calculations()
        heads, tails = calculations.counts(data)
        print(heads, tails)

        head_frac, tail_frac = calculations.fractions(heads, tails)
        print(head_frac, tail_frac)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
