def printPaths(path, maze, r, c, paths):
    if r == len(maze)-1 and c == len(maze[0])-1:
        paths.append(path)
        return
    if maze[r][c] == 0:
        return paths
    if r < len(maze)-1:
        printPaths(path+"V", maze, r+1, c, paths)
    if c < len(maze[0])-1:
        printPaths(path+"H", maze, r, c+1, paths)
    if r < len(maze)-1 and c < len(maze[0])-1:
        printPaths(path+"D", maze, r+1, c+1, paths)
    return paths

maze = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

print(printPaths("", maze, 0, 0, []))