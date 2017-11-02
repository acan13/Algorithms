from fractions import Fraction,gcd


def answer2(m):
    """
    The first method I tried was to brute force solve it by simulating a piece
    of ore a large number of times and then counting how many ended of in
    each state.

    The answers I got were pretty inconsistent, so next I tried solving it by
    using the probabilities, starting with 1 and then dividing that 1 into all
    of the places it could end up by running a number of rounds. That got me
    very close, but I had to approximate since a small fraction will always end
    up back in the transient states. This worked for all tests except #9.

    I couldn't get that to work even though I must have been close, so I looked
    into other options and found the absorbing Markov chain, which is basically
    what this is. You can solve the matrix easily by doing some matrix math,
    but I couldn't get the NumPy library so I had to create the methods myself.
    This worked for everything except case 4, which through trial and error, I
    discovered to be a 1x1 matrix. I solved this by including a simple if
    statement at the beginning.
    """

    if len(m) == 1:
        return [1,1]

    # this uses the same method as is used to solve an absorbing Markov chain
    # following the equation A = (I - Q)^-1 * R
    # A is the answer
    # t is the number of transient states
    # s is the number of absorbing states
    # Q is a t x t matrix consisting of the transient state relationships
    # R is a t x s matrix consisting of when transient states go directly to stable states
    # I is the t x t identity matrix

    # creates an index of which rows are terminal
    w = len(m)
    terminals = [True]*w

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


    # creates an identity matrix of the same size as I_min_Q
    # adds it to the right side of I_min_Q to prepare for next step
    inverse_m_row = [Fraction(0)]*len(I_min_Q)
    inverse_m = []
    for i in range(len(I_min_Q)):
        inverse_m.append(inverse_m_row[:])
        inverse_m[i][i] = Fraction(1)
        I_min_Q[i] +=  inverse_m[i][:]

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

    for i in range(len(I_min_Q)):
        for j in range(i+1,len(I_min_Q)):
            if I_min_Q[i][j] != 0:
                temp = I_min_Q[i][j]
                for k in range(j,len(I_min_Q[0])):
                    I_min_Q[i][k] -= temp * I_min_Q[j][k]

    # grabs the inverse of I_min_Q that we solved for
    inverse_m = []
    for i in range(len(I_min_Q)):
        inverse_m.append(I_min_Q[i][len(I_min_Q):])

    # grabs R from the ordered_m
    R = []
    for i in range(len(inverse_m)):
        R.append(ordered_m[i][len(inverse_m):])

    # solves for A, but only the first line since all the fuel starts
    # in the 0'th state

    A = []
    for j in range(len(R[0])):
        total = 0
        for i in range(len(R)):
            total += inverse_m[0][i] * R[i][j]
        A.append(total)

    # Converts A into the form that we want

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

m2 = [
  [0,1,1,0,0,0],
  [0,0,0,0,0,0],
  [3,0,0,2,1,1],
  [0,0,1,0,0,1],
  [0,0,0,0,0,0],
  [0,0,0,0,0,0],
]

m3 = [
  [0,0,1,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
]



# answer is 6,1,2,9

m4 = [[0,1],[0,0]]

m5 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

m6 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

m7 = [
  [0,2,1,0,0],
  [1,0,2,2,0],
  [3,1,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,0],
]

mm1 = [[0]]

print answer2(mm1)
