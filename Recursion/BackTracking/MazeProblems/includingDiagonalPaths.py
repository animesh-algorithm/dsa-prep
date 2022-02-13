def printPaths(path, r, c, paths):
    if r == 1 and c == 1:
        paths.append(path)
        return
    if r > 1:
        printPaths(path+"V", r-1, c, paths)
    if c > 1:
        printPaths(path+"H", r, c-1, paths)
    if r > 1 and c > 1:
        printPaths(path+"D", r-1, c-1, paths)
    return paths

print(printPaths("", 3, 3, []))