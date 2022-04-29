def Sublists(arr,n):

    Smallest_array=[0]*2
    Largest_array=[0]*(n-2)
    Smallest_sum=0
    Largest_sum=0
    arr.sort()


    for i in range (2):
        Smallest_array[i]=arr[i]
        Smallest_sum += Smallest_array[i]

    n = len(arr)
    for i in range(2,n):
        Largest_array[i-2]=arr[i]
        Largest_sum += arr[i]


    print ("The Large array: ",Largest_array," ,Sum = ",Largest_sum)
    print("The Small array: ", Smallest_array," ,Sum = ",Smallest_sum)



#Detecting errors
x=True
y=True
n=0
while (n<4 or x==True):
    try:
        arr = list(map(int, input("Enter the array: ").split()))
        n = len(arr)
        x=False
    except:
        print("Enter array of integers minimmun 4 numbers")


Sublists(arr,n)

