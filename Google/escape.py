from random import randint



def answer(entrances, exits, path):
    l = len(path)
    path = [[path[x][y] for y in range(l)] for x in range(l)]
    if len(exits) == 0 or len(entrances) == 0 or len(path) == len(entrances) + len(exits) or len(path) == 0:
        return 0

    # print 'original path'
    # print path,'\n'

    # just in case any locations have capacity to themselves
    for i in range(l):
        path[i][i] = 0
    # print 'path after removing capacity to same locations'
    # print path,'\n'

    # finds dead ends and removes the paths to them
    # counts the entrances as dead ends since it's never advantageous to go to them
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

    # print 'dead ends:',dead_ends

    for row in range(l):
        for position in range(l):
            if dead_ends[position] and path[row][position] != 0:
                path[row][position] = 0

    # print 'path modified for dead ends'
    # print path,'\n'

    # keeps track of where bunnies are
    current_bunnies = [ 0 for i in range(l)]

    # initializes current_bunnies with full paths from entrances
    for entrance in entrances:
        for num in range(l):
            current_bunnies[num] += path[entrance][num]
    # print 'current bunnies after paths from entrances'
    # print current_bunnies,'\n'

    # does some weighting to influence where bunnies go
    weights = []
    for row in path:
        weight = 0
        for exit in exits:
            weight += row[exit]
        weights.append(weight)
    weights2 = []
    for num in range(l):
        weights2.append(0)
        for pos in range(l):
            weights2[-1] += .5*path[num][pos]*weights[pos]
    weighted = [weights[i]+weights2[i] for i in range(l)]
    for entrance in entrances:
        weighted[entrance] = 0
    # print 'weighted'
    # print weighted,'\n'


    # initializes a solution (perhaps not the best)
    # runs until there is no more change
    # in other words, runs until reaching steady-state
    changes = current_bunnies[:]
    available_bunnies = [0 for i in range(l)]
    used_spots = [[0 for i in range(l)] for j in range(l)]
    controller = [[0 for i in range(l)] for j in range(l)]
    # print 'running test'
    # print 'used spots before'
    # print used_spots
    # print 'current_bunnies before'
    # print current_bunnies



    def test(path, entrances, exits, current_bunnies, controller):
        changes = current_bunnies[:]
        available_bunnies = [0 for i in range(l)]
        used_spots = [[0 for i in range(l)] for j in range(l)]
        # print 'used spots before'
        # print used_spots
        # print 'current_bunnies before'
        # print current_bunnies

        while sum(changes) != 0:
            available_bunnies = [available_bunnies[i]+changes[i] for i in range(l)]
            changes = [0 for i in range(l)]
            for location in range(l):
                # if capacity available at this location
                if sum(path[location]) != sum(used_spots[location]) and available_bunnies[location] != 0:
                    # first, if more bunnies than capacity, fill all
                    if available_bunnies[location] > sum(path[location])-sum(used_spots[location]):
                        for new_location in range(l):
                            # add bunnies to changes for new location
                            changes[new_location] += path[location][new_location] - used_spots[location][new_location]
                            # add bunnies to current_bunnies
                            current_bunnies[new_location] += path[location][new_location] - used_spots[location][new_location]
                            # remove bunnies from available of current location
                            available_bunnies[location] -= path[location][new_location] - used_spots[location][new_location]
                            # changes capacity to 0
                            used_spots[location][new_location] = path[location][new_location]
                            # sets the path to the current location as 0 since capacity is now 0
                            ### not including this line for now since capacity could be changed later
                            # path[new_location][location] = 0
                    else:
                        #first fill any paths to exits
                        if sum([used_spots[location][exit] for exit in exits]) != sum(path[location][exit] for exit in exits):
                            for exit in exits:
                                if available_bunnies[location] != 0:
                                    if available_bunnies[location] < path[location][exit] - used_spots[location][exit]:
                                        # add bunnies to changes for new location
                                        changes[exit] += available_bunnies[location]
                                        # add bunnies to current_bunnies
                                        current_bunnies[exit] += available_bunnies[location]
                                        # change capacity to new location
                                        used_spots[location][exit] += available_bunnies[location]
                                        # remove bunnies from availability of current location
                                        available_bunnies[location] = 0
                                    else:
                                        # add bunnies to changes for new location
                                        changes[exit] += path[location][exit]-used_spots[location][exit]
                                        # add bunnies to current_bunnies
                                        current_bunnies[exit] += path[location][exit]-used_spots[location][exit]
                                        # remove bunnies from availability of current location
                                        available_bunnies[location] -= path[location][exit]-used_spots[location][exit]
                                        # change capacity to new location
                                        used_spots[location][exit] = path[location][exit]
                        # now divy out the remaining bunnies

                        if available_bunnies[location] != 0:
                            new_location = entrances[-1] + 1
                            if new_location == location:
                                new_location += 1
                            while available_bunnies[location] != 0 and new_location != l:
                                if new_location == location:
                                    new_location += 1
                                # print 'location:',location
                                # print 'new_location:',new_location
                                if path[location][new_location] - used_spots[location][new_location] != 0:
                                    if available_bunnies[location] < path[location][new_location] - used_spots[location][new_location]:
                                        # add bunnies to changes for new location
                                        changes[new_location] += available_bunnies[location]
                                        # add bunnies to current_bunnies
                                        current_bunnies[new_location] += available_bunnies[location]
                                        # change capacity to new location
                                        used_spots[location][new_location] += available_bunnies[location]
                                        # remove bunnies from availability of current location
                                        available_bunnies[location] = 0
                                    else:
                                        # add bunnies to changes for new location
                                        changes[new_location] += path[location][new_location]-used_spots[location][new_location]
                                        # add bunnies to current_bunnies
                                        current_bunnies[new_location] += path[location][new_location]-used_spots[location][new_location]
                                        # remove bunnies from availability of current location
                                        available_bunnies[location] -= path[location][new_location]-used_spots[location][new_location]
                                        # change capacity to new location
                                        used_spots[location][new_location] = path[location][new_location]
                                new_location += 1

        # print 'used spots after'
        # print used_spots
        # print 'current_bunnies after'
        # print current_bunnies

        return current_bunnies



    tested = test(path, entrances, exits, current_bunnies, controller)

    high = sum([current_bunnies[exit] for exit in exits])






    # print 'saved bunnies:',sum([current_bunnies[exit] for exit in exits])
    return sum([tested[exit] for exit in exits])










    # finds the max number that can be saved
    # max_end = []
    # for gate in path:
    #     max_end.append(0)
    # for end in exits:
    #     for row in range(len(path)):
    #         max_end[row] += path[row][end]
    # max_to_save = sum(max_end)
    # print 'max to save:',max_to_save



    # if there are any bunnies in a position to be saved, it saves them and modifies the paths accordingly



    # def save_bunnies(path, current_bunnies, exits, saved):
    #     l = len(path)
    #     for row in range(l):
    #         if current_bunnies[row] > 0:
    #             for exit in exits:
    #                 if path[row][exit] >= current_bunnies[row]:
    #                     saved +=  current_bunnies[row]
    #                     path[row][exit] -= current_bunnies[row]
    #                     current_bunnies[row] = 0
    #                 elif path[row][exit] != 0:
    #                     saved += path[row][exit]
    #                     current_bunnies[row] -= path[row][exit]
    #                     path[row][exit] = 0
    #     print 'after save position saves'
    #     print 'current bunnies',current_bunnies
    #     print 'path',path
    #     print 'saved',saved,'\n'
    #     return saved

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



    # def step(path, current_bunnies, exits):
    #     l = len(path)
    #
    #     for row in range(l):
    #         if current_bunnies[row] > sum(path[row]):
    #             for new_location in range(l):
    #                 current_bunnies[row] -= path[row][new_location]
    #                 current_bunnies[new_location] += path[row][new_location]
    #                 path[row][new_location] = 0
    #         else:
    #             while current_bunnies[row] != 0:
    #                 rand = randint(0,l-1)


    # print 'weighting'
    # print weighting(path, entrances, exits)
    # saved = save_bunnies(path, current_bunnies, exits, saved)
    # step(path, current_bunnies, exits)
    # saved = save_bunnies(path, current_bunnies, exits, saved)

    # x = 0
    # while x != 1000:
    #     step(path, current_bunnies, exits)
    #     saved = save_bunnies(path, current_bunnies, exits, saved)
    #     x += 1



    # print path
    # biggest_pipe = []
    # for gate in path:
    #     biggest_pipe.append(0)
    # print biggest_pipe
    #
    # for entrance in entrances:
    #     for location in range(len(path)):
    #         biggest_pipe[location] += path[entrance][location]
    #
    #
    #
    # max_flow = []
    # for gate in path:
    #     max_flow.append(0)
    # for row in range(len(path)):
    #     for next_row in range(len(path)):
    #         max_flow[next_row] += path[row][next_row]
    #
    # max_end = []
    # for gate in path:
    #     max_end.append(0)
    # for end in exits:
    #     for row in range(len(path)):
    #         max_end[row] += path[row][end]
    #
    # print max_flow
    # print max_end
    #
    # return True


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
        [0, 0, 0, 0, 9, 9],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
        ]
}

test4 = {
    'entrances':[0, 1],
    'exits':[5],
    'path':[
        [0, 0, 4, 0, 5, 0],  # Room 0: Bunnies
        [0, 0, 0, 7, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 5, 0, 3],  # Room 2: Intermediate room
        [0, 0, 0, 0, 0, 4],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [11, 0, 0, 11, 0, 0],  # Room 5: Escape pods
        ]
}

test5 = {
    'entrances':[0, 1],
    'exits':[4,5],
    'path':[
        [0, 0, 0, 0, 0, 0],  # Room 0: Bunnies
        [0, 0, 0, 0, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 10, 10, 0],  # Room 2: Intermediate room
        [0, 0, 10, 0, 10, 0],  # Room 3: Intermediate room
        [0, 0, 10, 10, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 10, 10, 0],  # Room 5: Escape pods
        ]
}


test = test2

# print test

print answer(test['entrances'], test['exits'], test['path'])

# for i in range(5000):
#     print 'test #',i
#     test = []
#     size = randint(3,50)
#     # print size
#     for x in range(size):
#         row = []
#         for y in range(size):
#             rand = randint(0,6)
#             if rand == 0:
#                 row.append(randint(0,10))
#             if rand == 1:
#                 row.append(randint(0,100))
#             if rand == 2:
#                 row.append(randint(0,1000))
#             if rand == 3:
#                 row.append(randint(0,10000))
#             if rand == 4:
#                 row.append(randint(0,100000))
#             if rand == 5:
#                 row.append(randint(0,2000000))
#             if rand == 6:
#                 row.append(0)
#         test.append(row)
#         row = []
#
#     entrances = range(0,randint(1,size - 2))
#     # print entrances
#     exits = range(randint(len(entrances)+1,size-1),size)
#     try:
#         answer(entrances,exits,test)
#     except Exception as e:
#         print '\n\n\n\n\n\n'
#         print 'error:',e
#         print 'size:',size
#         print 'entrances:',entrances
#         print 'exits:',exits
#         print 'test:'
#         print test
#         break
# print 'finished'
