from fractions import Fraction,gcd


def answer2(m):

    # this uses the same method as is used to solve an absorbing Markov chain
    # t is the number of transient states
    # s is the number of absorbing states
    # Q is a t x t matrix
    # R is a t x s matrix
    # I is the t x t identity matrix

    w = len(m)
    terminals = [True]*w


    # creates an index of which rows are terminal
    for row in range(w):
        for i in range(w):
            if m[row][i] != 0:
                terminals[row] = False


    # creates an index of the new order of the rows in the matrix
    order = []
    order2 = []
    for i in range(w):
        if terminals[i]:
            order2.append(i)
        else:
            order.append(i)
    order+=order2

    # print terminals
    # print order

    # creates a new matrix with all the transient rows on top and terminal rows on bottom
    # converts the numbers to fraction probabilities
    ordered_m = []
    ordered_row = []
    for i in range(w):
        for j in range(w):
            if not terminals[order[i]]:
                ordered_row.append(Fraction(m[order[i]][order[j]],sum(m[order[i]])))
            else:
                ordered_row = [Fraction(0)]*w
        ordered_m.append(ordered_row[:])
        ordered_row = []

    print ordered_m

    # this pulls the I - Q matrix from the ordered_m matrix
    Q_row = []
    I_min_Q = []

    for i in range(terminals.count(False)):
        for j in range(terminals.count(False)):
            Q_row.append(Fraction(0))
            if i == j:
                Q_row[-1] = Fraction(1)
            Q_row[-1] -= ordered_m[i][j]
        I_min_Q.append(Q_row)
        Q_row = []


    print 'i minus q',I_min_Q,'\n'


    # creates an identity matrix of the same size as I_min_Q
    # adds it to the right side of I_min_Q to prepare for next step
    inverse_m_row = [Fraction(0)]*len(I_min_Q)
    inverse_m = []
    for i in range(len(I_min_Q)):
        inverse_m.append(inverse_m_row[:])
        inverse_m[i][i] = Fraction(1)
        I_min_Q[i] +=  inverse_m[i][:]

    print 'i min q with identity',
    for i in I_min_Q:
        print i
    print '\n'

    # finds inverse of I_min_Q by reducing to the identity matrix
    for i in range(len(I_min_Q)):
        for j in range(0,i):
            if I_min_Q[i][j] != 0:
                temp = I_min_Q[i][j] / I_min_Q[j][j]
                for k in range(j,len(I_min_Q[0])):
                    I_min_Q[i][k] -= temp * I_min_Q[j][k]
        if I_min_Q[i][i] != 1:
            temp = I_min_Q[i][i]
            for j in range(i,len(I_min_Q[0])):
                I_min_Q[i][j] /= temp
    print 'diagonal I minus Q'
    for i in I_min_Q:
        print i

    for i in range(len(I_min_Q)):
        for j in range(i+1,len(I_min_Q)):
            if I_min_Q[i][j] != 0:
                temp = I_min_Q[i][j]
                for k in range(j,len(I_min_Q[0])):
                    I_min_Q[i][k] -= temp * I_min_Q[j][k]

    print '\nfinal form'
    for i in I_min_Q:
        print i

    # grabs the inverse of I_min_Q that we solved for
    inverse_m = []
    for i in range(len(I_min_Q)):
        inverse_m.append(I_min_Q[i][len(I_min_Q):])

    print 'inverse'
    for i in inverse_m:
        print i
    print '\n'

    # grabs R from the ordered_m
    R = []
    for i in range(len(inverse_m)):
        R.append(ordered_m[i][len(inverse_m):])


    print 'R'
    for i in R:
        print i
    print '\n'


    # solves for A, but only the first line since all the fuel starts
    # in the 0'th state

    A = []
    for j in range(len(R[0])):
        total = 0
        for i in range(len(R)):
            total += inverse_m[0][i] * R[i][j]
        A.append(total)

    print 'A',A

    denominators = []
    numerators = []

    for i in range(len(A)):
        denominators.append(A[i].denominator)
        numerators.append(A[i].numerator)

    # finds the least common multiple of the denominators
    lcm = denominators[0]
    for i in range(1,len(denominators)):
        g = gcd(lcm,denominators[i])
        lcm *= denominators[i]/g

    # modifies the numerators according to the lcm and appends the lcm
    for i in range(len(denominators)):
        numerators[i] *= lcm/denominators[i]
        denominators[i] = lcm

    numerators.append(lcm)

    return numerators



m = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]



print 'final answer',answer2(m)


def answer(m):
    w = len(m)
    terminals = [True]*w

    for row in range(w):
        for i in range(w):
            if m[row][i] != 0:
                terminals[row] = False

    # the following method basically approximates the answer by running it
    # until reaching a predetermined precision

    results = [Fraction(0)]*w
    current = [Fraction(0)]*w
    current[0] = Fraction(1)
    precision = 6

    while sum(current) > 10**-precision:
        # print 'current',current
        # print 'results',results,'\n'
        for i in range(w):
            if terminals[i]:
                results[i] += current[i]
                current[i] = Fraction(0)
            else:
                row_total = sum(m[i])
                sum_to_distribute = current[i]
                for j in range(w):
                    current[j] += sum_to_distribute * Fraction(m[i][j],row_total)
                    current[i] -= sum_to_distribute * Fraction(m[i][j],row_total)

    # the following takes the results and approximates them to a more friendly scale
    # the liklihood of error here should be very small on this scale
    # then makes a list of the numerators and denominators of the terminal states
    numerators = []
    denominators = []

    for i in range(w):
        if terminals[i]:
            results[i] = results[i].limit_denominator(100000)
            numerators.append(results[i].numerator)
            denominators.append(results[i].denominator)

    # finds the least common multiple of the denominators
    lcm = denominators[0]
    for i in range(1,len(denominators)):
        g = gcd(lcm,denominators[i])
        lcm *= denominators[i]/g

    # modifies the numerators according to the lcm and appends the lcm
    for i in range(len(denominators)):
        numerators[i] *= lcm/denominators[i]
        denominators[i] = lcm

    numerators.append(lcm)

    return numerators



m = [
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]

m2 = [
  [0,1,1,0,0,0],
  [0,0,0,0,0,0],
  [3,0,0,2,1,1],
  [0,0,1,0,0,1],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
]


print answer(m2)

# print answer2(m)
