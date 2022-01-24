name = input('Enter File: ')
handle = open(name)

#make dictionary
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#bigcount = None
#bigword = None
#for word, count in counts.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count
x=list()
#x=sorted(counts.items())
#x=counts.items()
for a,b in counts.items():
    y=(b,a)
    x.append(y)
#print ('flipped',x)
x= sorted(x, reverse=True)
#print('Sorted: ',x[:3])
for b,a in x[:5]:
    print (a,b)
    









