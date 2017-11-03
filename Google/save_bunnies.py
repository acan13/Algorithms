from random import randint
def answer(times,time_limit):

    w = len(times)
    for i in range(w):
        if times[i][i] < 0:
            return range(w-2)

    def shortest_times(times,start,shortest = [],count = 0):
        """
        This is used to change the given times matrix to reflect the
        actual shortest travel times, including routes through other nodes
        that may be shorter than a direct route.

        Knowing the shortest path will allow easier code later, and will
        expose infinite loops.

        It is based off an algorithm I found called the Bellman-Ford
        that acts similarly to Dijkstra but can handle negative distances.
        """
        if count == len(times) - 1:
            return shortest
        count += 1

        if shortest == []:
            shortest = [9999]*len(times)
            shortest[start] = 0

        for i in range(len(times)):
            for j in range(len(times)):
                if shortest[i] + times[i][j] < shortest[j]:
                    shortest[j] = shortest[i] + times[i][j]

        return shortest_times(times,start,shortest,count)

    for i in range(w):
        times[i] = shortest_times(times,i)

    # print 'final times'
    # for i in times:
    #     print i
    # print '\n'

    def rescue_bunnies(times,current_pos,remaining_time,visited_locations = [], bunnies_rescued = []):
        # print 'current_pos:',current_pos, 'remaining_time:',remaining_time
        #should run at most (len(times)-1)*2 times

        # deep copy
        visited_locations = visited_locations[:]
        bunnies_rescued = bunnies_rescued[:]

        # add current location to visited_locations unless at the bulkhead
        if not current_pos in visited_locations and current_pos != len(times)-1:
            visited_locations.append(current_pos)

        # quit if you can't reach the bulkhead with time for it to be open
        if remaining_time < times[current_pos][-1]:
            # print 'dead end, bunnies_rescued',bunnies_rescued, '\n'
            return bunnies_rescued

        # save bunnies if at the bulkhead while it's open
        if current_pos == len(times)-1 and remaining_time >= 0:
            bunnies_rescued = visited_locations[:]
            if 0 in bunnies_rescued:
                bunnies_rescued.remove(0)
            bunnies_rescued = [x-1 for x in bunnies_rescued]
            bunnies_rescued.sort()
            # print 'saved bunnies:',bunnies_rescued

        # quit if you've rescued all of the bunnies
        if len(bunnies_rescued) == len(times) - 2:
            return bunnies_rescued

        possible_results = []

        # can now visit any location not yet visited, or the bulkhead if not already on it
        for new_pos in range(len(times)):
            if new_pos != current_pos and not new_pos in visited_locations:
                possible_results.append(rescue_bunnies(times,new_pos,remaining_time-times[current_pos][new_pos],visited_locations,bunnies_rescued))

        # print 'possible results',possible_results

        max_length = 0
        for result in possible_results:
            if len(result) > max_length:
                max_length = len(result)
        possible_results = [x for x in possible_results if len(x) == max_length]
        possible_results.sort()
        return possible_results[0]


    return rescue_bunnies(times,0,time_limit)








times1 = [[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]]
time_limit1 = 1

times2 = [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]]
time_limit2 = 3

times3 = [
[0,1,1,1,1,1,1],
[1,0,1,1,1,1,1],
[1,1,0,1,1,1,1],
[1,1,1,0,1,1,1],
[1,1,1,1,0,1,1],
[1,1,1,1,1,0,1],
[1,1,1,1,1,1,0]
]
time_limit3 = 99

times4 = [
[0,2,2,2,2,2,-1],
[7,0,7,7,7,7,-1],
[2,2,0,2,2,2,-1],
[2,2,2,0,2,2,-1],
[2,2,2,2,0,2,-1],
[2,2,2,2,2,0,-1],
[2,2,2,2,2,2,0],
]

time_limit4 = 1

times5 = [
[0,2,2,2,2,2,-1],
[2,0,2,2,-1,2,2],
[2,2,0,2,2,2,1],
[2,2,2,0,2,2,-1],
[2,2,-1,2,0,2,1],
[2,2,2,2,2,0,-1],
[2,-1,2,2,2,2,0],
]

time_limit5 = 2

times6 = [
[0,-1],
[1,0]
]

time_limit6 = 1

print '%'*400
print answer(times2,time_limit2)
"""
testing
"""
# broken_maps = []
#
# for test in range(500000):
#     print 'test',test
#     size = randint(2,2)
#     time = randint(-200,200)
#     test_map = []
#     for i in range(size):
#         row = []
#         for j in range(size):
#             row.append(randint(-100,100))
#         test_map.append(row)
#     if not answer(test_map,time):
#         broken_maps.append(test_map)
# print 'there were',len(broken_maps), 'maps that broke'
# print 'the maps that broke it'
# for test_map in broken_maps:
#     for row in test_map:
#         print row
#     print '\n'
