#ex_06_01 - Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted string into 
# a floating point number.

str = 'XDSPAM-Confidence: 0.8475  '
colpos = str.find (':')
# print (colpos)
newstr = str[colpos+1:]
# print (newstr)
num = float (newstr)
print (num)
