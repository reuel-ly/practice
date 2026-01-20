def stringToList(string):
    word=[]
    for char in string:
        word.append(char)
    return word
        
def solution(text, ending):
    endingList, checkList, j = stringToList(ending), [], 0
    location = len(endingList)
    
    for i in text:
        if j >= len(text) - location:
            checkList.append(i)     
        j+=1
    
    if checkList == endingList:
        return True
    else:
        return False