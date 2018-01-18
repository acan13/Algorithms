def one_away(str1, str2):
    if type(str1) != type(str2) or type(str1) != str:
        return False
    if str1 == str2:
        return True
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        for i in xrange(len(str1)):
            if str1[:i] + str1[i+1:] == str2[:i] + str2[i+1:]:
                return True

    else:
        if len(str1) > len(str2):
            for i in xrange(len(str1)):
                if str1[:i] + str1[i+1:] == str2:
                    return True
        else:
            for i in xrange(len(str2)):
                if str2[:i] + str2[i+1:] == str1:
                    return True
    return False

print one_away('pale','ple')
print one_away('pales','pale')
print one_away('pale','bale')
print one_away('pale','bake')

def one_away2(str1, str2):
    if type(str1) != type(str2) or type(str1) != str:
        return False
    if str1 == str2:
        return True
    if abs(len(str1) - len(str2)) > 1:
        return False

    for i in xrange(len(str1)+1):
        if i == len(str1) or i == len(str2):
            return True
        if str1[i] != str2[i]:
            if str1[i+1:] == str2[i:] or str2[i+1:] == str1[i:] or str1[i+1:] == str2[i+1:]:
                return True
            else:
                return False

print one_away2('pale','ple')
print one_away2('pales','pale')
print one_away2('pale','bale')
print one_away2('pale','bake')
