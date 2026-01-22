def cakes(recipe, available):
    recipe_cat = list(recipe.keys())
    possible_cook = float('inf') 
    
    
    for i in recipe_cat:
        if i not in available:
            return 0
            
        possible_cook = min(possible_cook, available[i] // recipe[i])  
    
    
    
    return possible_cook