# 1. Basic - Print all integers from 0 to 150

for x in range(0,151):
    print(x)

# 2. Multiples of five - Print all multiples of 5 from 5 to 1,000

for x in range (5,1001,5):
    print(x)

# 3. Counting the dojo way - Print integers 1 to 100. If divisible by 5, print "Coding" and if divisible by 10, print "Coding Dojo"

for x in range (1,101):
    if (x % 10 == 0):
        print('Coding Dojo')
    
    elif (x % 5 == 0):
        print('Coding')
    
    else:
        print(x)
    

# 4. Whoa. That sucker's huge

hugeSucker = 0

for x in range(0, 500000):
    if (x % 2 == 1):
        hugeSucker += x
print(hugeSucker)

# 5. Countdown by Fours

for x in range(2018, 0, -4):
    if (x % 2 == 0):
        print(x)

# 6. Flexible Counter

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1):
    if (x % mult == 0):
        print(x)