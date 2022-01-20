s = "baccad"

def remove(s, res):
    if s == "":
        return res
    if s[0] != "a":
        res += s[0]
    return remove(s[1:], res)

def remove(s):
    if s == "":
        return s
    if s[0] != "a":
        return s[0] + remove(s[1:])
    return remove(s[1:])

print(remove(s))