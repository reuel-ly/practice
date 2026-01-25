# Digits
def zero(func = None):
    try:
        n, operation = func
        print("0")
        if operation == "+":
            return 0 + n
        if operation == "-":
            return 0 - n
        if operation == "x":
            return 0 * n
        if operation == "/":
            return 0 // n

    except TypeError:
        return 0
def one(func = None):
    try:
        n, operation = func
        print("one")
        if operation == "+":
            return 1 + n
        if operation == "-":
            return 1 - n
        if operation == "x":
            return 1 * n
        if operation == "/":
            return 1 // n

    except TypeError:
        return 1    

def two(func=None): 
    try:
        n, operation = func
        print("two")
        if operation == "+":
            return 2 + n
        if operation == "-":
            return 2 - n
        if operation == "x":
            return 2 * n
        if operation == "/":
            return 2 // n

        else:
            return 2

    except TypeError:
        return 2

def three(func=None): 
    try:
        n, operation = func
        print("three")
        if operation == "+":
            return 3 + n
        if operation == "-":
            return 3 - n
        if operation == "x":
            return 3 * n
        if operation == "/":
            return 3 // n

        else:
            return 3

    except TypeError:
        return 3

def four(func=None): 
    try:
        n, operation = func
        print("four")
        if operation == "+":
            return 4 + n
        if operation == "-":
            return 4 - n
        if operation == "x":
            return 4 * n
        if operation == "/":
            return 4 // n

        else:
            return 4

    except TypeError:
        return 4

def five(func=None): 
    try:
        n, operation = func
        print("five")
        if operation == "+":
            return 5 + n
        if operation == "-":
            return 5 - n
        if operation == "x":
            return 5 * n
        if operation == "/":
            return 5 // n

        else:
            return 5

    except TypeError:
        return 5

def six(func=None): 
    try:
        n, operation = func
        print("six")
        if operation == "+":
            return 6 + n
        if operation == "-":
            return 6 - n
        if operation == "x":
            return 6 * n
        if operation == "/":
            return 6 // n

        else:
            return 6

    except TypeError:
        return 6

def seven(func=None): 
    try:
        n, operation = func
        print("seven")
        if operation == "+":
            return 7 + n
        if operation == "-":
            return 7 - n
        if operation == "x":
            return 7 * n
        if operation == "/":
            return 7 // n

        else:
            return 7

    except TypeError:
        return 7

def eight(func=None): 
    try:
        n, operation = func
        print("eight")
        if operation == "+":
            return 8 + n
        if operation == "-":
            return 8 - n
        if operation == "x":
            return 8 * n
        if operation == "/":
            return 8 // n

        else:
            return 8

    except TypeError:
        return 8

def nine(func=None): 
    try:
        n, operation = func
        print("nine")
        if operation == "+":
            return 9 + n
        if operation == "-":
            return 9 - n
        if operation == "x":
            return 9 * n
        if operation == "/":
            return 9 // n

        else:
            return 9

    except TypeError:
        return 9

# --------------- operations -------------------
def plus(n): #your code here
    print("addition", n)
    return n, "+"

def minus(n): #your code here
    print("minus", n)
    return n, "-"

def times(n): #your code here
    print("addition", n)
    return n, "x"

def divided_by(n): #your code here
    print("division", n)
    return n, "/"
