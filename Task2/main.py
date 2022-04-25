import math
def division(arr,n):
    array1=[]
    array2=[]
    half=""
    for i in range (n):
        length=len(arr[i])
        x=math.ceil(length/2)
        string1=slice(0,x)
        string2=slice(x,length)
        array1.append(arr[i][string1])
        array2.append(arr[i][string2])
    print(array1,array2)



arr = input("Enter the array: ").split()
n=len(arr)

division(arr,n)
