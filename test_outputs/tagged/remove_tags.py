import sys
import re

with open(sys.argv[1], 'r') as f:
    for line in f:
        if 'REW' in line:
            l = line.rstrip()
            words = l.split()
            removed = list(filter(lambda word: 'REW' not in word, words))
            txt = ' '.join(removed)
            print(re.sub(r'\s([?.!"](?:\s|$))', r'\1', txt))
        else:
            print(re.sub(r'\s([?.!"\'](?:\s|$))', r'\1', line), end='')


