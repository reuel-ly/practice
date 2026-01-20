def likes(names):
    
    size = len(names)
    
    if size == 0:
        return "no one likes this"
    
    elif size == 1:
        return f"{names[0]} likes this"
    elif size == 2:
        return f"{names[0]} and {names[1]} like this"
    elif size == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif size > 3:
        return f"{names[0]}, {names[1]} and {size - 2} others like this"
        
    
    pass