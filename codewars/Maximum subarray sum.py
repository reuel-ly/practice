def max_sequence(arr):
    if len(arr) == 0:
        return 0
    
    
    current = arr[0]
    maximum = arr[0]
    
    
    
    for i in range(1, len(arr)):
        current = max(arr[i], current + arr[i])
        
        if current > maximum:
            maximum = current
            
    return maximum if maximum > 0 else 0