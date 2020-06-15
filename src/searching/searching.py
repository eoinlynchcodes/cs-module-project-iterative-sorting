def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    low, high = 0, len(arr) -1
    while low <= high:
        middle = (low + high)
        if arr[middle] < target:
            low = middle + 1
        elif target < arr[middle]:
            high = middle - 1
        else:
            return middle

    return -1  # not found