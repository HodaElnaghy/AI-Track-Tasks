def Rotations(arr,n,k):
    arr_of_rotates=[0] * n
    for i in range(n):
        arr_of_rotates[i] = arr[i]

    for i in range(n):
        arr_of_rotates[(i+k)%n]=arr[i]

    return (arr_of_rotates)
arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)
k= int(input("Enter the number of rotations: "))
print("The array after Rotations: ",Rotations(arr,n,k))
