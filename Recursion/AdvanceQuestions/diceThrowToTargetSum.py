dice = [1, 2, 3, 4, 5, 6]

def diceThrow(p, target, res):
    if target == 0:
        res.append(p)
        return res
    for num in dice:
        if num <= target:
            diceThrow(p*10+num, target-num, res)
    return res

print(diceThrow(0, 4, []))