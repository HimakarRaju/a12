from bubblesort import bubblesort


def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 1, 3, 4, 5, 6, 3, 165, 20, 54, 23, 11, 65, 345, 243, 3542, 7654, 7654, 34343, 5]
sorted_arr = set(bubblesort(arr))
to_find = 11
print(sorted_arr, to_find)
