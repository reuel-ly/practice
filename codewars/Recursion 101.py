def solve(a,b):
    # step i
    if a == 0 or b == 0:        
        return [a,b]
    
    # step ii
    elif a >= (2 * b):  
        return solve((a - (2*b)), b)
     
    # step iii
    elif b >= (2 * a):
        return solve(a, (b - (2*a)))
    
    else:
        return [a,b]