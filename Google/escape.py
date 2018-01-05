from random import randint



def answer(entrances, exits, path):
    l = len(path)

    #need to add something to get rid of paths to same location

    # finds and marks bad locations (dead ends)
    dead_ends = []
    for num in range(l):
        dead_ends.append(False)
    for row in range(l):
        if sum(path[row]) == 0:
            dead_ends[row] = True
    for exit in exits:
        dead_ends[exit] = False
    for entrance in entrances:
        dead_ends[entrance] = True

    print 'dead ends:',dead_ends

    # removes paths to dead ends
    for row in range(l):
        for position in range(l):
            if dead_ends[position] and path[row][position] != 0:
                path[row][position] = 0

    print 'path modified for dead ends'
    print path

    # keeps track of where bunnies are
    current_bunnies = [ 0 for i in range(l)]

    # initializes current_bunnies with full paths from entrances
    for entrance in entrances:
        for num in range(l):
            current_bunnies[num] += path[entrance][num]

    # runs fill_funnel until there is no more change in current_bunnies
    # in other words, runs until reaching steady-state
    changes = current_bunnies[:]
    used_spots = [[0 for i in range(l)] for j in range(l)]
    while sum(changes) != 0:
        available_bunnies = [available_bunnies[i]+changes[i] for i in range(l)]
        changes = [0 for i in range(l)]
        for location in range(l):
            # if capacity available at this location
            if sum(path[location] != sum(used_spots[location])):
                # first, if more bunnies than capacity, fill all
                if available_bunnies[location] > sum(path[location])-sum(used_spots[location]):
                    for new_location in range(l):
                        # add bunnies to changes for new location
                        changes[new_location] += path[location][new_location] - used_spots[location][new_location]
                        # remove bunnies from available of current location
                        available_bunnies[location] -= path[location][new_location] - used_spots[location][new_location]
                        # changes capacity to 0
                        used_spots[location][new_location] = path[location][new_location]
                        # sets the path to the current location as 0 since capacity is now 0
                        path[new_location][location] = 0








    # print [ [0 for x in range(len(path))] for i in range(len(path))]



    def fill_funnel(path, entrances, exits):
        controller = [ [0 for x in range(len(path))] for i in range(len(path))]

        print 'controller'
        print controller

        while steps != len(path)

    print 'starting path'
    print path


    # if there are any paths from an entrance to an exit, adds these bunnies to the saved bunnies
    # actually this is useless since they will never overlap
    for entrance in entrances:
        for exit in exits:
            saved += path[entrance][exit]


    print '\n'

    # finds the max number that can be saved
    max_end = []
    for gate in path:
        max_end.append(0)
    for end in exits:
        for row in range(len(path)):
            max_end[row] += path[row][end]
    max_to_save = sum(max_end)
    print 'max to save:',max_to_save



    # if there are any bunnies in a position to be saved, it saves them and modifies the paths accordingly

    def save_bunnies(path, current_bunnies, exits, saved):
        l = len(path)
        for row in range(l):
            if current_bunnies[row] > 0:
                for exit in exits:
                    if path[row][exit] >= current_bunnies[row]:
                        saved +=  current_bunnies[row]
                        path[row][exit] -= current_bunnies[row]
                        current_bunnies[row] = 0
                    elif path[row][exit] != 0:
                        saved += path[row][exit]
                        current_bunnies[row] -= path[row][exit]
                        path[row][exit] = 0
        print 'after save position saves'
        print 'current bunnies',current_bunnies
        print 'path',path
        print 'saved',saved,'\n'
        return saved

    def weighting(path, entrances, exits):
        weights = []
        for row in path:
            weight = 0
            for exit in exits:
                weight += row[exit]
            weights.append(weight)
        # don't need the next lines probably
        # for exit in exits:
        #     weights.append(99999999999)
        return weights



    def step(path, current_bunnies, exits):
        l = len(path)

        for row in range(l):
            if current_bunnies[row] > sum(path[row]):
                for new_location in range(l):
                    current_bunnies[row] -= path[row][new_location]
                    current_bunnies[new_location] += path[row][new_location]
                    path[row][new_location] = 0
            else:
                while current_bunnies[row] != 0:
                    rand = randint(0,l-1)


    print 'weighting'
    print weighting(path, entrances, exits)
    saved = save_bunnies(path, current_bunnies, exits, saved)
    step(path, current_bunnies, exits)
    saved = save_bunnies(path, current_bunnies, exits, saved)

    # x = 0
    # while x != 1000:
    #     step(path, current_bunnies, exits)
    #     saved = save_bunnies(path, current_bunnies, exits, saved)
    #     x += 1


    print 'final saved:',saved





    return saved












    print path
    biggest_pipe = []
    for gate in path:
        biggest_pipe.append(0)
    print biggest_pipe

    for entrance in entrances:
        for location in range(len(path)):
            biggest_pipe[location] += path[entrance][location]



    max_flow = []
    for gate in path:
        max_flow.append(0)
    for row in range(len(path)):
        for next_row in range(len(path)):
            max_flow[next_row] += path[row][next_row]

    max_end = []
    for gate in path:
        max_end.append(0)
    for end in exits:
        for row in range(len(path)):
            max_end[row] += path[row][end]

    print max_flow
    print max_end

    return True


test1 = {
    'entrances':[0],
    'exits':[3],
    'path':[[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
}

test2 = {
    'entrances':[0, 1],
    'exits':[4,5],
    'path':[
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
        ]
}

test3 = {
    'entrances':[0, 1],
    'exits':[4,5],
    'path':[
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 9, 9],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
        ]
}

test = test3

# print test

print answer(test['entrances'], test['exits'], test['path'])
