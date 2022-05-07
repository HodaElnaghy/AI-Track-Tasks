def target_4(arr,target):

    for x in range (len(arr)):

        for y in range(x+1,len(arr)):

            for z in range(y+1,len(arr)):

                for h in range(z+1, len(arr)):
                    if (arr[x] + arr[y] + arr[z] + arr[h] == target):

                        return (arr[x], arr[y], arr[z],arr[h])
    return False





arr = list(map(int, input("Enter the array: ").split()))
target= int(input("enter target: "))
target1=target+1
while(1):
    if(target_4(arr,target)!=False):
        print("Integers: ",target_4(arr,target))
        break
    elif (target_4(arr,target)!=False):
        print("Integers: ",target_4(arr, target))
        break
    else:
        if (target>3):
            target-=1
        target1+=1
