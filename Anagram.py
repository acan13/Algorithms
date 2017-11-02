def anagram(string,arr=[]):
    # breaks up each input into [already anagrammed,yet to be anagrammed]
    if arr == []:
        arr = ["",string]
    temp = []

    # if yet to be anagrammed has only 1 thing, returns the combined values
    # of anagrammed and yet to be anagrammed
    if len(arr[1]) == 1:
        return [arr[0]+arr[1]]

    # if yet to be anagrammed has more than one thing, loops through each
    # character in yet to be anagrammed, adding it to anagrammed and then
    # running the function on the remaining characters in yet to be anagrammed
    for i in range(len(arr[1])):
        temp += anagram("", [arr[0]+arr[1][i], arr[1][:i]+arr[1][i+1:]])
    return temp

print anagram("ABCD")
