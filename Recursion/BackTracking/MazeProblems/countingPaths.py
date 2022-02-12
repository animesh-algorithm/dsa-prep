def countPaths(r, c):
    if r == 1 or c == 1:
        return 1
    return countPaths(r-1, c) + countPaths(r, c-1)

print(countPaths(3,3))