fin = open('C:\\Users\\Ani\\Downloads\\dataset_2_7.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

string = fin.readline().replace('\n','').split(' ')[0]
pattern = fin.readline().replace('\n','')
k = len(pattern)

count = 0

for i in range(0,len(string)-k+1):
    if string[i:i+k] == pattern:
        count += 1

fout.write(str(count))

fin.close()
fout.close()
