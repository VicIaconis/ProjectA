# ex_07_01 Write a program to read through a file and print the contents of the file
# (line by line) in all  upper case to match sample from:
# https://www.youtube.com/watch?v=il1j4wkte2E

cnt = 0
fh = open ('Project1\ex_07_01\mbox-short.txt')
for lx in fh:

# return full data as uppercase, single spaced info
#    ly = lx.rstrip()
#    print (ly.upper())

# identify specific lines and locations from Steve
#    cnt = cnt + 1
#    ly = lx.upper()
#    if ly.startswith ('FROM STEPHEN'):
#        print ("Line",cnt,":",ly.rstrip())
#print ('Line Count: ',cnt)
    
# identify specific line from ex_06_01 - line 45 /success!
    cnt = cnt + 1
    ly = lx.upper()
    if ly.startswith ('X-DSPAM-CONFIDENCE: 0.8475'):
        print ("Line",cnt,":",ly.rstrip())