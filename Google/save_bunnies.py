def answer(times,time_limit):
    w = len(times)
    for i in range(w):
        if times[i][i] < 0:
            return range(w-2)

    def shortest_times(times,start,shortest = [],count = 0):
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

    print 'final times'
    for i in times:
        print i
    print '\n'


    def rescue_bunnies(times,current_pos,remaining_time,bunnies_grabbed = [],bunnies_rescued = []):
        # if len(bunnies_rescued) == len(times)-2:
        #     return bunnies_rescued
        bunnies_grabbed = bunnies_grabbed[:]
        bunnies_rescued = bunnies_rescued[:]
        # print 'currently at',current_pos,'remaining time:', remaining_time
        # end if you can't get to the bulkhead in time
        if remaining_time < times[current_pos][len(times)-1]:
            return bunnies_rescued

        # add bunnies grabbed to rescued bunnies if you are at the bulkhead
        if current_pos == len(times) - 1 and remaining_time >= 0:
            # print 'rescued some bunnies:',bunnies_grabbed
            for bunny in bunnies_grabbed:
                bunnies_rescued.append(bunny)
            bunnies_rescued = list(set(bunnies_rescued))
            bunnies_rescued.sort()
        # grab a bunny if you're at their location and haven't rescued them yet
        elif current_pos > 0 and current_pos not in bunnies_rescued:
            # print 'grabbed a bunny:',current_pos
            bunnies_grabbed.append(current_pos)

        if len(bunnies_rescued) == len(times)-2:
            return bunnies_rescued

        possible_results = []

        for new_pos in range(len(times)):
            if new_pos != current_pos and new_pos not in bunnies_grabbed and new_pos not in bunnies_rescued and new_pos != 0:
                possible_results.append(rescue_bunnies(times,new_pos,remaining_time - times[current_pos][new_pos],bunnies_grabbed,bunnies_rescued))

        # print 'possible_results',possible_results


        max_length = 0
        for result in possible_results:
            # print 'this should not be more than one deep?',result
            if len(result) > max_length:
                max_length = len(result)

        for i in range(len(possible_results)):
            if len(possible_results[i]) < max_length:
                possible_results[i] = "EXTERMINATE!"

        while "EXTERMINATE!" in possible_results:
            possible_results.remove("EXTERMINATE!")

        possible_results.sort()
        # print 'processed possible_results',possible_results
        final_result = possible_results[0]
        return final_result



    is_this_it = rescue_bunnies(times,0,time_limit)
    # print 'final result:', is_this_it
    here = [x-1 for x in is_this_it]
    return here








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
[]
]

print '%'*400
print answer(times5,time_limit5)
