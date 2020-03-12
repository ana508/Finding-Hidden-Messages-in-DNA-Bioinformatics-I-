inpt = open('C:\\Users\\Ani\\Downloads\\dataset_2_7.txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

string = inpt.readline().replace('\n','').split(' ')[0]
pattern = inpt.readline().replace('\n','')
k = len(pattern)

count = 0

for i in range(0,len(string)-k+1):
    if string[i:i+k] == pattern:
        count += 1

output.write(str(count))

inpt.close()
output.close()
