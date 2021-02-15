from numpy import random
import os
import winsound

## Frequency and duration for the beep sound
frequency = 2000  # Set Frequency To 2000 Hertz
duration = 100  # Set Duration // 1000 ms == 1 second

##generating random values from 1 to 9, where each number represents a foreground color of the windows command prompt or shell

c = random.choice([1,2,3,4, 5,6, 7,8, 9])
color_string = "color "

## This will generate a list of random floating numbers of 5 items for infinite time
while True:
    c = random.choice([1,2,3,4, 5,6, 7,8, 9])
    x = random.rand(1,5)
    color_s = color_string+str(c)
    os.system(color_s)
    print(x)
    os.system(color_s)
    print('\a') ## this is unnecessary but I kept it for no reason
    winsound.Beep(frequency, duration)


## Color codes for windows command prompt
# 0 = Black       8 = Gray
# 1 = Blue        9 = Light Blue
# 2 = Green       A = Light Green
# 3 = Aqua        B = Light Aqua
# 4 = Red         C = Light Red
# 5 = Purple      D = Light Purple
# 6 = Yellow      E = Light Yellow
# 7 = White       F = Bright White