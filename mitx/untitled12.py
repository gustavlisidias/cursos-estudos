def getSublists(L, n):
    """
    It returns a list of all possible sublists in L of length n without skipping elements in L.
    
    :param L: a list of integers
    :param n: the length of the sublists
    """

    a = []
    for i in range(len(L) - (n-1)):
        a.append(L[i:i+n])
    return a

L = [1, 1, 1, 1, 4]
print(getSublists(L, 2))