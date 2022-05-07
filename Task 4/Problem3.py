def binary_search(arr, low, high, x):
    if high==low:
        if arr[high]>x:
            return high
        else:
            return high+1
    if high > low:
        mid = (high + low) // 2
        if arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return  arr


def Index_search(arr,target):
    if target in arr:
        return arr.index(target)
    return -1

arr = list(map(int, input("Enter the array: ").split()))
target=int(input("Enter target: "))
if Index_search(arr,target)!=-1:
    print("Index is:",Index_search(arr,target))

else:
    print("Sorted array is:", insertionSort(arr))
    print("Index is:" ,binary_search(arr,0,len(arr)-1,target))

