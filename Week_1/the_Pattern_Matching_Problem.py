inpt = open('C:\\Users\\Ani\\Downloads\\dataset_3_5.txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')
pattern = inpt.readline().replace('\n','').split(' ')[0]
text = inpt.readline().replace('\n','')

t = {i:text[i] for i in range(0,len(text)-len(pattern)+1) if text[i:i+len(pattern)]==pattern}

nums = []
for num in t.keys():
    nums.append(str(num))

output.write(' '.join(nums))

inpt.close()
output.close()