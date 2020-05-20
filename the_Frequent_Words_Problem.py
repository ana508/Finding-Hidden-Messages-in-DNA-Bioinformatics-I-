fin = open('C:\\Users\\Ani\\Downloads\\dataset_2_10.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
txt = fin.readline().replace('\n','').split(' ')
k = int(txt[0])
string = fin.readline().replace('\n','')

from collections import Counter

patterns = []
for i in range(0,len(string)-k+1):
    pattern = string[i:i+k]
    patterns.append(pattern)
    result = Counter(patterns)

max_count = 0
for i in result:
    if result[i] > max_count:
        max_count = result[i]
        most_frequent_letter = i

fout.write(most_frequent_letter)

fin.close()
fout.close()