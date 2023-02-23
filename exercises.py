# Write a function is_triangular that meets the specification below. 
# A triangular number is a number obtained by the continued summation of integers starting from 1. 
# For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    triangulars = []

    for i in range(1, k+1):
        if i == 1:
            triangulars.append(1)
        else:
            triangulars.append(i + triangulars[-1])

    return k in triangulars


# Write a Python function that creates and returns a list of prime numbers between 2 and N, inclusive, sorted in increasing order. 
# A prime number is a number that is divisible only by 1 and itself. This function takes in an integer and returns a list of integers.

def primes_list(N):
    '''
    N: an integer
    '''
    lista = []

    def isprime(num):
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True

    for i in range(2, N+1):
        if isprime(i):
            lista.append(i)

    return lista

primes_list(178)


# Implement a function that meets the specifications below.
# For example, cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

def cipher(map_from, map_to, code):
    """ 
    map_from, map_to: strings where each contain N unique lowercase letters. 
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where 
    each key is a letter in map_from at index i and the corresponding 
    value is the letter in map_to at index i. 
    decoded is a string that contains the decoded version 
    of code using the key_code mapping. 
    """
    key_code = {}
    decoded = ''
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for j in code:
        decoded += key_code[j]
    return key_code, decoded


# As written, this code leads to an infinite loop when using the Arrogant Professor class.
# Change the definition of ArrogantProfessor so that the following behavior is achieved

class Person(object):     
    def __init__(self, name):         
        self.name = name     

    def say(self, stuff):         
        return self.name + ' says: ' + stuff    

    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Person): 
    def say(self, stuff): 
        return self.name + ' says: ' + 'It is obvious that ' + self.name + ' says: ' + stuff

    def lecture(self, stuff):
        return 'It is obvious that ' + self.name + ' says: ' + stuff





class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.dictionary = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.k = k
        self.v = v
        isThere = False
        if len(self.dictionary) == 0:
            self.dictionary += [[k, v]]
            isThere = True

        for item in self.dictionary:
            if k == item[0]:
                item[1] = v
                isThere = True

        if isThere == False:
            self.dictionary += [[k, v]]

    def getval(self, k):
        for item in self.dictionary:
                if item[0] == k:
                    return item[1]
        raise KeyError

    def delete(self, k):
        """ k, immutable object """
        count = False
        for item in self.dictionary:
            if k == item[0]:
                del item[:]
                self.dictionary = [x for x in self.dictionary if x != []]
                count = True
        if count == False:
            raise KeyError


    def drukuj(self):
        return print(self.dictionary)