#Have user guess a preselected number
#target = 7

#randomize number

import random
target = random.randint(1,20)

attempt = 0
guess = 999999
name = input("What's your name")

while guess != target:
    
    guess = int(input("guess a number between 1 and 20!"))
    attempt = attempt + 1
    if (guess>target):
            print ('sorry,', name,". That's too high") 
    if (guess==target):
            print ('Yay', name, 'You did it!', target, 'was the correct number. It took you',attempt, 'tries.')
    if (guess<target):
            print ('sorry,', name,". That's too low")
     



