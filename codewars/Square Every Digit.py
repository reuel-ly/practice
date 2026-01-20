def square_digits(num):
    numList = []
    strAnswer = ""
    
    for i in str(num):
        temp = int(i)**2
        numList.append(str(temp))
        
    for i in numList:
        
        strAnswer += i
        
    return int(strAnswer)