#Given a list of integers write a function to sort the list 
#and another to return the first and last appearance of a given target number in the sorted list
def First_Last_Index(arr,n,target):
    index1= arr.index(target)
    arr.reverse()
    index2= n-1-arr.index(target)
    return (index1, index2)


def Sorting(arr,n,target):
    arr.sort()
    return(First_Last_Index(arr,n,target))

arr = list(map(int, input("Enter the array: ").split()))
target=int(input("Enter the target number: "))
n=len(arr)
print(Sorting(arr,n,target))
