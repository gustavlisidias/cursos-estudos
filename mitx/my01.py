# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:46:14 2022

@author: GDias
"""

#s = "azcbobobegghakl"
#longest = s[0]
#current = s[0]
#for c in s[1:]:
#    if c >= current[-1]:
#        current += c
#        if len(current) > len(longest):
#            longest = current
#    else:
#        current = c
#print('Longest substring in alphabetical order is: ', longest)
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons)) 
