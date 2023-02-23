def validacao(n1, n2, op):
    try:
        int(n1)
    except:
        return "Error: Numbers must only contain digits."
    
    try:
        int(n2)
    except:
        return "Error: Numbers must only contain digits."

    if len(n1) >= 5 or len(n2) >= 5:
        return "Error: Numbers cannot be more than four digits."

    if op != '+' and op != '-':
        return "Error: Operator must be '+' or '-'."

    return None

def imprimir(arr, res=True):    
    for f in arr:
        print(f'{f[0]:>6}', end=' '*5)

    print('')
    for f in arr:
        print(f'{f[2]:<}{f[1]:>5}', end=' '*5)

    print('')
    for f in arr:
        if   len(f[0]) == 4 or len(f[1]) == 4:
            print(f'------', end=' '*5)
        elif len(f[0]) == 3 or len(f[1]) == 3:
            print(f' -----', end=' '*5)
        elif len(f[0]) == 2 or len(f[1]) == 2:
            print(f'  ----', end=' '*5)
        else:
            print(f'   ---', end=' '*5)

    if res:
        print('')
        for f in arr:
            print(f'{f[3]:>6}', end=' '*5)

def arithmetic_arranger(lst, prt=False):
    new_lst = []

    try:
        if len(lst) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    
    for i in lst:
        n1  = i.split()[0]
        n2  = i.split()[2]
        op  = i.split()[1]      
        
        exp = validacao(n1, n2, op)
        
        if exp is not None:
            return exp     
        
        if op == '-':
            rs = int(n1) - int(n2)
        else:
            rs = int(n1) + int(n2)

        if prt:
            new_lst += [[n1, n2, op, rs]]
        else:
            new_lst += [[n1, n2, op]]
        
    return imprimir(new_lst, prt)