def add(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add([1,2,3,4,5,6,7,8,9,10]))