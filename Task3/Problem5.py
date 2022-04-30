def Targetnumbers(arr,n,Target):
    indexes=[]
    remainder = Target

    #Checking on the first number
    for j in range(n):
        remainder=Target
        del indexes[:]
        remainder-= arr[j]
        indexes.append(j)

        #Checking on the second number
        for i in range (j+1,n):
            if len(indexes)<4:
                if (arr[i]<=remainder):
                    indexes.append(i)
                    remainder -=arr[i]

                    #Checking on the third number
                    for x in range (i+1,n):
                        if len(indexes) < 4:
                            if (arr[x] > remainder):
                                remainder+= arr[x-1]
                                indexes.pop()
                            if (arr[x] <= remainder):
                                indexes.append(x)
                                remainder -= arr[x]
                                #Checking if we finally found our target numbers
                                if (remainder == 0 and len(indexes) == 3):
                                    return indexes
                    for h in range(1,len(indexes)):
                        remainder += arr[indexes[len(indexes)-1]]
                        indexes.pop()



    #if the main for loop ended before finding the target 3 numbers then the array doesn't contain our target numbers
    return ("There are no 3 numbers that you can add in this array to give you this target")

# Detecting errors
x = True
y = True
n = 0

while (x == True or y == True):
    try:
        arr = list(map(int, input("Enter the array: ").split()))
        n = len(arr)
        Target=int(input("Enter the Target number: "))
        x = False
    except:
        print("Enter array of integers minimmun 2 numbers")
    if (n > 2):
        y = False


print(Targetnumbers(arr,n,Target))
