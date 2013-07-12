#sets union
def union(a, b):
    res = []
    for e in a:
        if e not in b:
            res.append(e)
    return b + res

if '__name__' == '__main__':
    a = [1,3,5,7,8]
    b = [2,3,4,6,8]

    print union(a, b)
