inpt = open('C:\\Users\\Ani\\Downloads\\dataset_3_2.txt', 'r')
output = open('C:\\Users\\Ani\\OneDrive\\Desktop\\output.txt', 'w')

text = inpt.readline().replace('\n','')

text = text[::-1]

def complementary(text):
    complement= {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    list_of_nuc = []
    for nuc in text:
        list_of_nuc.append(complement[nuc])
    return list_of_nuc

result = complementary(text)

output.write(''.join((result)))

inpt.close()
output.close()