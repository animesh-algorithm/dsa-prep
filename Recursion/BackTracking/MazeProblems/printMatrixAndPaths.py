# all direction are allowed

def printPaths(path, maze, r, c, paths, step):
    if r == len(maze)-1 and c == len(maze[0])-1:
        paths[r][c] = step
        for row in paths:
            for cell in row:
                print(cell, end="  ")
            print()
        print(path)
        return
    if maze[r][c] == 0:
        return
    maze[r][c] = 0
    paths[r][c] = step
    if r < len(maze)-1:
        printPaths(path+"D", maze, r+1, c, paths, step+1)
    if c < len(maze[0])-1:
        printPaths(path+"R", maze, r, c+1, paths, step+1)
    # if r < len(maze)-1 and c < len(maze[0])-1:
    #     printPaths(path+"D", maze, r+1, c+1, paths)
    if r > 0:
        printPaths(path+"U", maze, r-1, c, paths, step+1)
    if c > 0:
        printPaths(path+"L", maze, r, c-1, paths, step+1)
    # this line where the function will be over
    # so before the functions gets removed, also revert the changes back to previous state
    maze[r][c] = 1
    paths[r][c] = 0

maze = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]

paths = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

printPaths("", maze, 0, 0, paths, 1)