def isIn(char, aStr): # iterative
    aStr    = sorted(aStr)    
    minimum = 0
    maximum = len(aStr)
    middle  = (maximum + minimum) // 2
    
    while True:
        if char == aStr[middle]:
            return True
            break
        elif (minimum == middle == maximum - 1):
            return False
            break
        elif char > aStr[middle]:
            minimum = middle 
            middle  = (maximum + minimum) // 2
        elif char < aStr[middle]:
            maximum = middle 
            middle  = (maximum + minimum) // 2
        
    
print(isIn('g','ascending'))

def isIn(char, aStr): # recursive
   aStr = sorted(aStr)
   if aStr == '':
      return False

   if len(aStr) == 1:
      return aStr == char
  
   minimum = 0
   maximum = len(aStr)
   middle  = (maximum + minimum) // 2
   
   if char == aStr[middle]:
      return True

   elif char < aStr[middle]:
      return isIn(char, aStr[:middle])
   else:
      return isIn(char, aStr[middle+1:])
  
print(isIn('g','ascending'))