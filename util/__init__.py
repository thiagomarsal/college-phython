# Sort list
def sortHigh(list):
    list.sort()


# Sort list
def sortLow(list):
    list.sort(reverse=True)


# Remove duplicates
def removeDuplicate(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    return newlist