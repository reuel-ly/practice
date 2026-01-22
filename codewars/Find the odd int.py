import numpy as np
def find_it(seq):
    dict = {}
    
    for i in range(len(seq)):
        for j in range(len(seq)):
            if seq[i] == seq[j] and seq[i] not in dict:
                dict[seq[i]] = 1
            elif seq[i] == seq[j]:
                dict[seq[i]] += 1
                
    print(dict)
    return check_odd(dict)
    
def check_odd(dict):
    iter_dict = list(dict.keys())
    
    for i in iter_dict:
        if abs(dict[i]) % 2 != 0:
            return i