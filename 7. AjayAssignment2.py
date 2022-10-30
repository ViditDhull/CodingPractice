from string import punctuation
from collections import defaultdict
from operator import itemgetter


filename = input("Enter the file name: ")
with open(filename, 'r', encoding = 'utf-8') as f:
    text = f.read().lower()
    words = text.split()
    punc_translator = str.maketrans({key: None for key in punctuation})
    new = [i.translate(punc_translator) for i in words]
    
    

dist = []
for i in new:
    if i not in dist:
        dist.append(i)

dd = defaultdict(int)
for i in new:
    dd[i] += 1
    

dds = sorted(dd.items(), key = itemgetter(1), reverse = True)
print(type(dds))

ddc = defaultdict(int)
for i in new:
    for j in i:
        ddc[j] += 1
        
ddsc = sorted(ddc.items(), key = itemgetter(1), reverse = True)

with open("Summary.txt", "w", encoding = 'utf-8') as f:
    f.write("Total words: \n")
    for i in new:
        f.write(i + " ")
    f.write('\n')
    f.write("Total distinct words: \n")
    for i in dist:
        f.write(i + " ")
    f.write('\n')
    f.write("The top 25 most frequent words and counts: \n")
    for t in dds[:26]:
        line = ':'.join(str(x) for x in t)
        f.write(line + '\n')
    f.write('\n')
    f.write("Character frequency sorted from most frequent to least frequent character: \n")
    for t in ddsc:
        line = ':'.join(str(x) for x in t)
        f.write(line + '\n')