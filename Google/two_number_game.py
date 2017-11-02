from random import randint


#successfully submitted
def answer(M,F):
    M = long(M)
    F = long(F)

    if M == F:
        if M == 1:
            return "0"
        else:
            return  "same impossible"
    if M%2 == 0 and F%2 == 0:
        return "even impossible"

    if M == 1:
        return str(F-1)
    if F == 1:
        return str(M-1)

    if M < 1 or F < 1:
        return "normal impossible"

    if M%F == 0  or F%M == 0:
        return "divisible impossible"


    if M/F >= 1:
        count = int(M/F)
        M_prev = M - count*F
        F_prev = F
    else:
        count = int(F/M)
        F_prev = F - count*M
        M_prev = M

    try:
        return str(count+long(answer(M_prev,F_prev)))
    except:
         return "exception impossible"




"""
Everything below this was just for testing
"""


#print answer("2",str((10**50)-1))
# print answer("4","7")
for i in range(5000):
    a = randint(1,10**50)
    b = randint(1,10**50)
    print answer(str(99),str(b))

#
#
# def test():
#     a = long(1)
#     b = long(1)
#     a_limit = randint(1,10**50)
#     b_limit = randint(1,10**46)
#     count = long(0)
#     print 'a limit:',a_limit
#     print 'b limit:',b_limit
#
#     while a < a_limit or b < b_limit:
#         if a > a_limit:
#             b+=a
#         elif b > b_limit:
#             a+=b
#         else:
#             if randint(1,2) == 1:
#                 a+=b
#             else:
#                 b+=a
#         count+=1
#
#     return [a,b,count]
#
# counter=0
#
# for i in range(5000):
#     counter+=1
#
#
#     tester = test()
#     print str(tester[0]),':a'
#     print str(tester[1]),':b'
#     print str(tester[2]),':build count'
#
#     print answer(str(tester[0]),str(tester[1])), ':algo result'
#     print counter,':counter'
#
#     if str(tester[2]) != answer(str(tester[0]),str(tester[1])):
#         print '------------------------------------------------------------------'
#         break
#     print '\n'
