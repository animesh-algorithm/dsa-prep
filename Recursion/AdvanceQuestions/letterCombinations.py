mapping = {
            "2": "abc", 
            "3": "def", "4": "ghi", "5": "jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

digits = "23"
inp = [mapping[digits[i]] for i in range(len(digits))]

def letterCombinations(p, up, combos):
    if up == "":
        combos.append(p)
        return combos
    for i in range(len(mapping[up[0]])):
        letterCombinations(p+mapping[up[0]][i], up[1:], combos)
    return combos

print(letterCombinations("", "23", []))