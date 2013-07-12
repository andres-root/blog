#sets intersection
def intersection(a, b):
    res = []
    for e in a:
        if e in b:
            res.append(e)
    return res

if '__name__' == '__main__':
    a = [1,3,5,7,8]
    b = [2,3,4,6,8]

    print intersection(a, b)
