import os
from termgraph.termgraph import chart

# Print custom legend
print('\033[3mPies\033[0m      \033[1mBars\033[0m')  # Italic Pies, Bold Bars
# print('\033[3mPies\033[0m  \u25A0 \033[1mBars\033[0m  \u25A1')  # Italic Pies, Bold Bars, Grey and White Squares

args = {
    'filename': 'data.txt',
    'title': None,
    'width': 50,
    'format': '{:<5.2f}',
    'suffix': '',
    'no_labels': False,
    'color': [3, 2],  # white, grey
    'vertical': False,
    'stacked': False,
    'different_scale': False,
    'calendar': False,
    'start_dt': None,
    'custom_tick': '',
    'delim': '',
    'version': False,
    'bins': 0,
    'labels': [],
    'histogram': False,
    'no_values': False,
}

# Read data and labels
with open('data.txt') as f:
    lines = f.readlines()
    labels = []
    data = []
    for line in lines[1:]:
        label, values = line.strip().split(':')
        values = list(map(float, values.strip().split()))
        labels.append(label)
        data.append(values)

args['labels'] = labels

if __name__ == "__main__":
    chart(colors=args['color'], data=data, labels=args['labels'], args=args)
