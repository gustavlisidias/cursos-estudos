import math

def polysum(n, s):
    '''
    n: Number of sides of the regular polygon
    s: Size of each side of the regular polygon
    
    returns the sum of area and perimetro rounded by 4 decimal places
    '''
    
    # According to the formula:
    area  = (0.25 * n * pow(s, 2)) / math.tan(math.pi / n)
    perimetro = pow((n * s), 2)
    
    return round((area + perimetro), 4)   

# Test:
print(polysum(32, 4))