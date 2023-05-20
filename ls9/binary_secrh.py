def binary_search(arr, target): 
    left, right = 0, len(arr) - 1

    while left <=right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1

    return left

own_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

a = binary_search(own_list, 5)
b = binary_search(own_list, 10)
c = binary_search(own_list, 15)

print(a, b, c)