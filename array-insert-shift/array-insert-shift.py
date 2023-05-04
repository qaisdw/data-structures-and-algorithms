def insertShiftArray(arr, val):
    mid = len(arr) // 2

    # if the length of the list is even, insert the value at the middle index of the array
    # else, insert it at the middle index + 1
    if len(arr) % 2 == 0:
        arr.insert(mid, val)
    else:
        arr.insert(mid+1, val)

    print(arr)
    return arr




def remove_middle(arr):
    mid = len(arr) // 2
    arr.pop(mid)
    print(arr)
    return arr




arr = [2,4,6,-8]
val = 16

insertShiftArray(arr,val)
# remove_middle(arr)