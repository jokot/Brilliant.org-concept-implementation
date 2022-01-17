
def quick_sort(arr):
    left_list = []
    right_list = []
    pivot_list = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        if len(arr) > 2:
            pivot = sorted([arr[0],arr[len(arr)//2],arr[-1]])[1]
        for a in arr:
            if a == pivot:
                pivot_list.append(a)
            elif a < pivot:
                left_list.append(a)
            else:
                right_list.append(a)
    return quick_sort(left_list)+pivot_list+quick_sort(right_list)

if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,8,9]
    arr = [3,5,1,7,9,4,8,6,2]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)