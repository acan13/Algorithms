def remove_spaces(string):
    space = string.find(' ')
    if space != -1:
        return remove_spaces(string[:space] + string[space+1:])
    return string

# def remove_spaces(string):
#     space = string.find(' ')
#     if space != -1:
# 		return remove_spaces(string[:space] + string[space+1:])
# 	return string

print remove_spaces('He llo M y  N a me    IsAllan   ')
