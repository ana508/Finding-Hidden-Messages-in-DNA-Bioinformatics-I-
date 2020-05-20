fin = open('C:\\Users\\Ani\\Downloads\\dataset_3_5.txt', 'r')
fout = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
pattern = fin.readline().replace('\n','').split(' ')[0]
text = fin.readline().replace('\n','')

t = {i:text[i] for i in range(0,len(text)-len(pattern)+1) if text[i:i+len(pattern)]==pattern}

nums = []
for num in t.keys():
    nums.append(str(num))

fout.write(' '.join(nums))

fin.close()
fout.close()