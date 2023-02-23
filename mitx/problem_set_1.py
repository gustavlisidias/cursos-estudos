s = 'azcbobobegghakl'
c = 0
for i in s:
    if i in 'aeiou':
        c += 1

print('Number of vowels:', c)

s = 'azcbobobegghaklbob'
c = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        c += 1

print('Number of times bob occurs is:', c)


s = 'azcbobobegghakl'
temp = s[0]
output = s[0]
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        temp = temp + s[i+1]
        
        if len(temp) > len(output):
            output = temp           
    else:
        temp = s[i+1]

print('Longest substring in alphabetic order is:' + output)