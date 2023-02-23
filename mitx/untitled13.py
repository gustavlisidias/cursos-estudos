def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    a = []
    for i in aDict.keys():
        if aDict[i] == target:
            a.append(i)
    return a