def Secondlargest(arr,n):
    largest=arr[0]
    Secondlargest=0
    counter=0
    for i in range(n):
        if (largest<arr[i]):

            Secondlargest=largest
            largest=arr[i]

        elif (Secondlargest<arr[i] and largest>arr[i]):
            Secondlargest = arr[i]


    return (Secondlargest)

def Secondsmallest(arr,n):
    smallest=arr[0]
    Secondsmallest=arr[n-1]

    for i in range(n):
        if (smallest>arr[i]):

            Secondsmallest=smallest
            smallest=arr[i]
        elif (Secondsmallest>arr[i] and smallest<arr[i]):
            Secondsmallest = arr[i]
    return (Secondsmallest)




arr = list(map(int, input().split()))
n= len(arr)
print("Second largest number is: ", Secondlargest(arr,n))
print("Second Smallest number is: ", Secondsmallest(arr,n))
