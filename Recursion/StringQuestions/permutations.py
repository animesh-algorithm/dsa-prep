s = 'abc'
def permutations(up, p):
    if up == "":
        return 1
    ch = up[0]
    count = 0
    for i in range(0, len(p)+1):
        f = p[:i]
        l = p[i:]
        count += permutations(up[1:], f+ch+l)
    return count

print(permutations(s, ""))