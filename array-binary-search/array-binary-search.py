# BinarySearch
def BinarySearch(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == value:
            return mid

        elif arr[mid] < value:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# object BinarySearch
def objectBinarySearch(arr, key, prop):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid][prop] == key:
            return mid
        elif arr[mid][prop] > key:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1



print(BinarySearch([-131, -82, 0, 27, 42, 68, 179], 42))