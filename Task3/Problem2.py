
is_even = lambda num : num%2

def even_count(arr):
    count=0
    for i in range(len(arr)):
        if (is_even(arr[i])==0):
            count+=1
    return count

arr = list(map(int, input("Enter the array: ").split()))
print(even_count(arr))
