xh = input('Enter Hours ')
hours = float (xh)
xr = input('Enter Rate ')
rate = float (xr)
if hours > 40:
    ot = hours-40
    print ('Overtime Hours',ot)
    xp = (40*rate)+(ot*(1.5*rate))
else :
    xp = hours*rate
print ("Pay",xp)