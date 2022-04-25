def isSymmetric(arr,n):
    for i in range(0, int(n/2)):
        if(arr[i]!=arr[n-1-i]):
            return False
    return True


arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)
if(isSymmetric(arr,n)):
    print("The set is symmetric")
else:
    print("The set is not symmetric")
