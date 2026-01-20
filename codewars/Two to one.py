def longest(a1, a2):
    letters = a1 + a2
    ansString = ""
    tempList = []
    
    # remove the duplicates
    [tempList.append(i) for i in letters  if i not in tempList]
    
    # bubble sort
    for i in range(len(tempList)):
        for j in range(len(tempList)):
            
            if ord(tempList[i]) < ord(tempList[j]):
                tempList[i], tempList[j] = tempList[j], tempList[i]
    
    
    for i in tempList:
        ansString += i
        
    return ansString