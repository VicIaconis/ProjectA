xh = input('Enter Hours')
xr = input('Enter Rate')
try:
    hours = float (xh)
    rate = float (xr)
except:
    print ('Error, please enter numeric input')
    quit()

if hours > 40:
    ot = hours-40
    print ('Overtime Hours',ot)
    xp = (40*rate)+(ot*(1.5*rate))
else :
    xp = hours*rate
print ("Pay",xp)