
def merge(left, right):
    left_idx = 0
    right_idx = 0
    result = []
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
    return merge(left,right)

if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,8,9]
    arr = [3,5,1,7,9,4,8,6,2]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)