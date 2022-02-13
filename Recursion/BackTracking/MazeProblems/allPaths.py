# all direction are allowed

def printPaths(path, maze, r, c, paths):
    if r == len(maze)-1 and c == len(maze[0])-1:
        paths.append(path)
        return
    if maze[r][c] == 0:
        return paths
    maze[r][c] = 0
    if r < len(maze)-1:
        printPaths(path+"D", maze, r+1, c, paths)
    if c < len(maze[0])-1:
        printPaths(path+"R", maze, r, c+1, paths)
    # if r < len(maze)-1 and c < len(maze[0])-1:
    #     printPaths(path+"D", maze, r+1, c+1, paths)
    if r > 0:
        printPaths(path+"U", maze, r-1, c, paths)
    if c > 0:
        printPaths(path+"L", maze, r, c-1, paths)
    # this line where the function will be over
    # so before the functions gets removed, also revert the changes back to previous state
    maze[r][c] = 1  
    return paths

maze = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

print(printPaths("", maze, 0, 0, []))