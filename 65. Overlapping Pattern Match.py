import re

def find_overlapping_indexes(text, pattern):
    
    regex = re.compile(f'(?=({pattern}))')
    return [(match.start(1), match.end(1)-1) for match in regex.finditer(text)]
    

text = input()
pattern = input()

indexes = find_overlapping_indexes(text, pattern)
if not indexes:
    print("(-1, -1)")
else:
    for idx in indexes:
        print(idx)