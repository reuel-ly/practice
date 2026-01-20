def solution(s):
    stringList = []
    
    for i in s:
        
        if i.isupper():
            stringList.append(f" {i}")     
        else:
            stringList.append(i)
    
    return addList(stringList)
                
    
def addList(s):
    stringAns = ""
    for i in s:
        stringAns += i
        
    return stringAns