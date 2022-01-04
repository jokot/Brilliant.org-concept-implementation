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

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binarySearch(3, a))
    print(binarySearch(9, a))
    print(binarySearch(11, a))