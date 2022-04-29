def First_Last_Index(arr,n,target):
    index1= arr.index(target)
    arr.reverse()
    index2= n-1-arr.index(target)
    return (index1, index2)


def Sorting(arr,n,target):
    arr.sort()
    return(First_Last_Index(arr,n,target))

is_even = lambda num : num%2

def even_count(arr):
    count=0
    for i in range(len(arr)):
        if (is_even(arr[i])==0):
            count+=1
    return count


if __name__ == '__main__':
    arr = list(map(int, input("Enter the array: ").split()))
    print(even_count(arr))
