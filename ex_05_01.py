#Write a program which repeatedly reads numbers until the user enters "done". Once
#"done" is entered, print out the total, count, and average of the numbers. if the 
#user enters anything other than a number, detect their mistake and print the error
#message and skip to the next number.

num = 0
tot = 0
while True:
    sval = input ('Enter a number: ')
    if sval == 'done' :
        break
    try:
        fval = float (sval)
    except:
        print ('Invalid input')
        continue     
    num = num + 1
    tot = fval + tot
    ave = tot / num
    continue
print (tot, num, ave)