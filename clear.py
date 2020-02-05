def setKey(str):
    if str[0] == "\"" and str[len(str) - 1] == "\"":
        return str[1: len(str) - 1]

    return str




def setValue(value):
    if value[0] == "\"" and value[len(value) - 1] == "\"":
        return int(value[1: len(value) - 1])
    elif value == "false":
        return False
    elif value == "true":
        return True




def clear(str):
    if str[0] == "{" and str[len(str) - 1] == "}":
        return str[1: len(str) - 1]





def strToDict(i):
    i = clear(i)
    newDict = dict()

    for items in i.split(","):
        key = setKey(items.split(":")[0])
        value = setValue(items.split(":")[1])

        newDict[key] = value

    return newDict