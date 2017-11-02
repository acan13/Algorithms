def answer(maze,top=True,check = [[0,0]]):

    to_check = [] #used to store the next nodes to check
    solutions = [] #used to store the various solutions to compare
    new_maze = [] #used to copy the maze
    h = len(maze)
    w = len(maze[0])

    # this loop modifies the maze to a more useful format (only for the first call)
    if top:
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == 0:
                    maze[i][j] = 9999
                if maze[i][j] == 1:
                    maze[i][j] = '*'
        maze[0][0] = 1


        # makes a deep copy of the maze
        for i in range(len(maze)):
            new_maze.append(maze[i][:])

        # calls the function on the maze with no walls destroyed
        # adds the solution to the solutions list
        solutions.append(answer(new_maze,False))

        # calls the function with each wall destroyed in succession
        # adds the result for each to the solutions list
        for y in range(len(maze)):
            for x in range(len(maze[0])):
                if maze[y][x] == '*':
                    new_maze = []
                    for i in range(len(maze)):
                        new_maze.append(maze[i][:])
                    new_maze[y][x] = 9999
                    solutions.append(answer(new_maze,False))


        # sorts the solutions and returns the lowest
        solutions.sort()
        return solutions[0]

    # this is more or less dijkstra's algorithm
    for item in check:
        x = item[1]
        y = item[0]

        if y-1 >= 0 and maze[y-1][x] != '*':
            if maze[y-1][x] > maze[y][x]+1:
                maze[y-1][x] = maze[y][x]+1
                to_check.append([y-1,x])
        if y+1 < h and maze[y+1][x] != '*':
            if maze[y+1][x] > maze[y][x]+1:
                maze[y+1][x] = maze[y][x]+1
                to_check.append([y+1,x])

        if x-1 >= 0 and maze[y][x-1] != '*':
            if maze[y][x-1] > maze[y][x]+1:
                maze[y][x-1] = maze[y][x]+1
                to_check.append([y,x-1])
        if x+1 < w and maze[y][x+1] != '*':
            if maze[y][x+1] > maze[y][x]+1:
                maze[y][x+1] = maze[y][x]+1
                to_check.append([y,x+1])

    if len(to_check) == 0:
        for item in maze:
            print item
        print '\n'
        return maze[-1][-1]
    return answer(maze,False,to_check)



maze1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print answer(maze1)
#print answer(maze2)
