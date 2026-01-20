def divisors(integer):
    answers = []
    
    for i in range(2, integer):
        if (integer % i) == 0:
            answers.append(i)
            
    
    
    if len(answers) == 0:
        return f"{integer} is prime"
    
    else:
        return answers