def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

my_list = [30, 20, 24, 13, 18, 9,35]
sorted_list = quick_sort(my_list)
print('Sorted Array are: ', sorted_list)