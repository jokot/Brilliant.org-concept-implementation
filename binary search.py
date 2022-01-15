def binarySearch(x, a):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo+hi) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid+1
        else:
            hi = mid-1
    return -1

def binarySearchRecursiveA(x, a, i=[]):
    if len(i) == 0:
        i = [0, len(a)]
    if i[0] == i[1]:
        return -1
    mid = (i[0]+i[1]) // 2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        i[0] = mid+1
    else:
        i[1] = mid-1
    return binarySearchRecursiveA(x, a, i)

def binarySearchRecursiveB(x, a, i=[]):
    if len(a) == 0:
        return -1
    else:
        listIndex = []
        if len(i) == 0:
            listIndex = [x for x in range(len(a))]
        else:
            listIndex = i.copy()
        mid = len(a) // 2
        # print(x, a, listIndex)
        if a[mid] == x:
            return listIndex[mid]
        elif a[mid] < x:
            return binarySearchRecursiveB(x, a[mid+1:], listIndex[mid+1:])
        else:
            return binarySearchRecursiveB(x, a[:mid], listIndex[:mid])

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearch(3, a))
    print(binarySearch(9, a))
    print(binarySearch(11, a))
    print(binarySearchRecursiveA(3, a))
    print(binarySearchRecursiveA(9, a))
    print(binarySearchRecursiveA(11, a))
    print(binarySearchRecursiveB(3, a))
    print(binarySearchRecursiveB(9, a))
    print(binarySearchRecursiveB(11, a))