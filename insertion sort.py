def insertionSort(a):
    for current in range(1, len(a)):
        i = current
        while i>0 and a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    return a

if __name__ == '__main__':
    a = [6,3,6,8,1,8,4,9,0,45,1,45,8,67,4,1,67,9]
    print(insertionSort(a))