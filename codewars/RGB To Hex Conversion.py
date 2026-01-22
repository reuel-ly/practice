def rgb(r, g, b):
    return (decimal_to_hex(r) + decimal_to_hex(g) + decimal_to_hex(b))


def decimal_to_hex(n):
    hex_dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    hex = ""
    remainder = 0
    
    if n == 0:
        return "00"
    elif n > 255:
        return "FF"
    elif n < 0:
        return "00"
    
    while n != 0:
        remainder = round(n % 16)
        n = n // 16 #quotient 

        if remainder < 10:
            hex += f"{remainder}"
        else:
            hex += hex_dict[remainder]
    if len(hex) == 1:
        hex += "0"
        
    return hex[::-1] #reverse the string