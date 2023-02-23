def recurPower(base, exp):
    if exp == 1:
        return base
    elif exp == 0 :
        return 1
    else:
        return base * recurPower((base), exp - 1)
    
    
def iterPower(base, exp):
    n = 1
    for i in range(exp):
        n = n * base
    return n

print(iterPower(3, 3))