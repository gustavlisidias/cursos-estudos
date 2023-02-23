
def gcdIter(a, b):
    i = 100
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1

print(gcdIter(9, 12))
    
def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print(gcdRecur(17, 12))