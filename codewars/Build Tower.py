def tower_builder(n):
    ansList = []
    space = n
    
    findOdd = ((2*n) - 1) #to get the base of the tower using the odd number series (2n - 1)
    spaceNumber = (((2*n) - 1) - 1)/2 # to get the spaces needed in the top
    
    for i in range(1, n + 1):        # count from 1 to the target number of floors
        asterisk = '*' * ((2*i)-1)   # count the odd number series from the start
    
        spacing = " " * int(spaceNumber) 
        spaceNumber -= 1             # decrement the amount of spacing
    
        ansList.append(f"{spacing}{asterisk}{spacing}")
        
    return ansList
        