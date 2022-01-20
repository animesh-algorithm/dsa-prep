s = "abc"

def subsetOfStr(s, subset, arr):
    if s=="":
        arr.append(subset)
        return arr
    subsetOfStr(s[1:], subset+s[0], arr)
    subsetOfStr(s[1:], subset, arr)
    return arr

print(subsetOfStr(s, "", []))