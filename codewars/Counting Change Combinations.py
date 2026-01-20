def count_change(money, coins):
    table = [0] * (money + 1)
    
    table[0] = 1
    
    for i in coins:
        for j in range(i, money + 1):
            table[j] += table[j - i]
    
    return table[money]