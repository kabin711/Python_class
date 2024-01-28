def Bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
my_list = [2, 99, 44, 55, 36]
Bubble_sort(my_list)
print(my_list)