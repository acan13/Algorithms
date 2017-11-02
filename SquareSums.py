from math import floor, sqrt
def SquareSum(N,step = -1,past=[]):
    if N == 0:
        return [past]
    if step == 0 or N < 0:
        return [-1]
    if step == -1:
        top = True
        step = int(floor(sqrt(N)))

    result = []
    for i in range(step,1,-1):
        branch = SquareSum(N-i*i,i-1,past+[i])
        if branch != [-1]:
            result+=branch
    return result

print SquareSum(68)
