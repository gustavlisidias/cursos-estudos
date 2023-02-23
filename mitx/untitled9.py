animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    count = 0
    for i in aDict.values():
        if len(i) > 1:
            for j in i:
                count += 1
        else:
            count += 1
    return count

print(how_many(animals))

def biggest(aDict):
    maximum = []
    for i in aDict.values():
        maximum.append(len(i))
        
    for k, v in aDict.items():
        if len(v) == max(maximum):
            return k

print(biggest(animals))