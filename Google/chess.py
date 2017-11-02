def answer(src,dest):

    def to_matrix(num):
        x = num % 8
        y = int(num/8)
        return [x,y]

    def to_num(xy):
        if xy[0] > 7 or xy[0] < 0:
            return -1
        if xy[1] > 7 or xy[1] < 0:
            return -1
        return xy[0] + xy[1]*8


    src_x = to_matrix(src)[0]
    src_y = to_matrix(src)[1]
    dest_x = to_matrix(dest)[0]
    dest_y = to_matrix(dest)[1]

    delta_x = dest_x - src_x
    delta_y = dest_y - src_y

    abs_dx = abs(delta_x)
    abs_dy = abs(delta_y)

    # same spot
    if src == dest:
        return 0

    # one move away
    if abs_dy == 1 and abs_dx == 2:
        return 1
    if abs_dx == 1 and abs_dy == 2:
        return 1

    # if diagonal from the destination
    if abs_dx == abs_dy:
        if abs_dx == 1:
            # if in the corners
            if dest == 0 or dest == 7 or dest == 56 or dest == 63:
                return 4
            else:
                return 2

    # if horizontal or vertical from the destination
    if delta_x == 0 or delta_y == 0:
        # if 1 space away
        if abs_dx == 1 or abs_dy == 1:
            return 3
        # if 2 spaces away
        if abs_dx == 2 or abs_dy == 2:
            return 2
        # if 3 spaces away
        if abs_dx == 3 or abs_dy == 3:
            return 3
        # if 4 spaces away
        if abs_dx == 4 or abs_dy == 4:
            return 2
        # if 5 spaces away
        if abs_dx == 5 or abs_dy == 5:
            return 3
        # if 6 spaces
        if abs_dx == 6 or abs_dy == 6:
            return 4
        # if 7 spaces
        if abs_dx == 7 or abs_dy == 7:
            return 5

    x_move = 1
    y_move = 1

    if delta_x < 0:
        x_move *= -1
    if delta_y < 0:
        y_move *= -1

    def distance(x1,y1,x2,y2):
        return pow(pow(x2-x1,2)+pow(y2-y1,2),.5)

    current_distance = distance(src_x,src_y,dest_x,dest_y)

    d1 = distance(src_x+x_move,src_y+2*y_move,dest_x,dest_y)
    d2 = distance(src_x+2*x_move,src_y+y_move,dest_x,dest_y)
    d3 = distance(src_x+2*x_move,src_y-y_move,dest_x,dest_y)
    d4 = distance(src_x-x_move,src_y+2*y_move,dest_x,dest_y)

    options = []

    if d1 < current_distance:
        options.append(to_num([src_x+x_move,src_y+2*y_move]))
    if d2 < current_distance:
        options.append(to_num([src_x+2*x_move,src_y+y_move]))
    if d3 < current_distance:
        options.append(to_num([src_x+2*x_move,src_y-y_move]))
    if d4 < current_distance:
        options.append(to_num([src_x-x_move,src_y+2*y_move]))

    results = []

    # print src_x,src_y
    # print options

    for option in options:
        if option != -1:
            results.append(1 + answer(option,dest))

    # print 'not sorted',results
    results.sort()
    # print 'sorted',results

    return results[0]




# print answer(0,1)

tester = []

for i in range(64):
    for j in range(64):
        tester.append(answer(i,j))

print tester
