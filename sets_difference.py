#sets diference
def difference(a, b):
    res = []
    for e in a:
        if e not in b:
            res.append(e)
    return res

if '__name__' == '__main__':
    a = [1,3,5,7,8]
    b = [2,3,4,6,8]

    print difference(a, b)
