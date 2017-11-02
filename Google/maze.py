def answer(maze):
    new_maze = []
    for i in range(len(maze)):
        new_maze.append(maze[i][:])

    x = 0
    y = 0
    destroyed_wall = False
    for i in range(len(new_maze)):
        if 9 in new_maze[i]:
            y = i
            x = new_maze[i].index(9)
            new_maze[y][x] = 2
            farthest = True
        if -1 in new_maze[i]:
            destroyed_wall = True
    if new_maze[y][x] == 0:
        new_maze[y][x] = 2

    h = len(maze)
    w = len(maze[0])
    results = []


    if x == w-1 and y == h-1:
        new_count = 0
        for item in new_maze:
            new_count+=item.count(2)
        return new_count+1

    if y+1 < h:
        if new_maze[y+1][x] == 0:
            new_maze[y+1][x] = 9

            results.append(answer(new_maze))
            new_maze[y+1][x] = 0
        if new_maze[y+1][x] == 1 and not destroyed_wall:
            new_maze[y+1][x] = 9
            new_maze[0][0] = -1

            results.append(answer(new_maze))
            new_maze[y+1][x] = 1
            new_maze[0][0] = 0

    if y-1 >= 0:
        if new_maze[y-1][x] == 0:
            new_maze[y-1][x] = 9

            results.append(answer(new_maze))
            new_maze[y-1][x] = 0
        if new_maze[y-1][x] == 1 and not destroyed_wall:
            new_maze[y-1][x] = 9
            new_maze[0][0] = -1

            results.append(answer(new_maze))
            new_maze[y-1][x] = 1
            new_maze[0][0] = 0

    if x+1 < w:
        if new_maze[y][x+1] == 0:
            new_maze[y][x+1] = 9

            results.append(answer(new_maze))
            new_maze[y][x+1] = 0
        if new_maze[y][x+1] == 1 and not destroyed_wall:
            new_maze[y][x+1] = 9
            new_maze[0][0] = -1

            results.append(answer(new_maze))
            new_maze[y][x+1] = 1
            new_maze[0][0] = 0

    if x-1 >= 0:
        if new_maze[y][x-1] == 0:
            new_maze[y][x-1] = 9

            results.append(answer(new_maze))
            new_maze[y][x-1] = 0
        if new_maze[y][x-1] == 1 and not destroyed_wall:
            new_maze[y][x-1] = 9
            new_maze[0][0] = -1

            results.append(answer(new_maze))
            new_maze[y][x-1] = 1
            new_maze[0][0] = 0

    # if none of the above were valid, return 9999 to signify dead end
    if results == []:

        return 9999

    results.sort()

    return results[0]

maze1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print answer(maze1)
print answer(maze2)
