from string import punctuation
from collections import defaultdict
from operator import itemgetter


filename = input("Enter the file name: ")
try:
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

    ddc = defaultdict(int)
    for i in new:
        for j in i:
            ddc[j] += 1

    ddsc = sorted(ddc.items(), key = itemgetter(1), reverse = True)

    if len(new) == 0:
        print("The file is empty.")
    else:
        print(f'The number of words in file are: {len(new)}')    
        print(f"The number of distinct words are: {len(dist)}")
        print(f"The top 25 most frequent words and counts: {dds[:26]}")
        print(f"Character frequency sorted from most frequent to least frequent character: {ddsc}")
except:
    print("The file could not be found.")