han = open('Project1\ex_08_01\mbox-short.txt')

for line in han:
    line = line.rstrip()
    #print('Line: ',line)
    
    if line == '' :
        #print('Skip Blank Line')
        continue
    wds = line.split()
    #print("Words:",wds)
    
    #Guardian Pattern using compound perameters
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    
    #if wds[0] != 'From ' :
        #print('Ignore')
        #continue
    print(wds[2])



#testing
#for x in han:
#    print (x)