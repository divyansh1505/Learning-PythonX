from functools import reduce
list = [1,45,67,32,4,23,17,8,34]

def greater(a, b):
    if (a>b):
        return a
    return b     
    
print(reduce(greater, list))