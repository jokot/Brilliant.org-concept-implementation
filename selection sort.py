def selectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

if __name__ == '__main__':
    a = [4,67,1,5,90,2,4,1,5,8,23,2,67,8,32,23,2,8,7,50,2,1,4,7]
    print(selectionSort(a))