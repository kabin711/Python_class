def insertation_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j] = key
my_list = [33, 32, 19, 12, 3, 4]
insertation_sort(my_list)
print('Sorted array are: ', my_list)