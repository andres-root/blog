from sets_intersection import *
from sets_union import *
from sets_difference import *

#sets symetric diference
def symmetric_difference(a, b):
    res = difference(union(a, b), intersection(a, b))
    return res

a = [1,3,5,7,8]
b = [2,3,4,6,8]

print symmetric_difference(a, b)
