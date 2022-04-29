def Sublists(arr,n):
    arr.sort()
    Smallest_array=[]
    Smallest_array_count=1

    Largest_array=[]
    Largest_array_count = 1
    Smallest_sum=0
    Largest_sum=0



    for i in range (n):
        if(Smallest_array_count<3):
            Smallest_array.append(arr[i])
            Smallest_sum += Smallest_array[i]
            Smallest_array_count+=1
        elif (Smallest_sum > Smallest_sum + arr[i]):
                Smallest_array.append(arr[i])
                Smallest_sum += Smallest_array[i]
        else: break


    arr.sort(reverse=True)

    for i in range (n):
        if(Largest_array_count<3):
            Largest_array.append(arr[i])
            Largest_sum += Largest_array[i]
            Largest_array_count+=1
        elif (Largest_sum < Largest_sum + arr[i]):
                Largest_array.append(arr[i])
                Largest_sum += Largest_array[i]
        else: break

    print("The Large array: ", Largest_array, " ,Sum = ", Largest_sum)

    print("The Small array: ", Smallest_array," ,Sum = ",Smallest_sum)



#Detecting errors
x=True
y=True
n=0
while(x==True or y==True):
    try:
        arr = list(map(int, input("Enter the array: ").split()))
        n = len(arr)
        x=False
    except:
        print("Enter array of integers minimmun 2 numbers")
    if (n>1):
        y=False

print(Sublists(arr,n))







