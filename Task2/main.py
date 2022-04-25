def indexs(arr,n,sum):
    first_index=0
    second_index=0
    second_value=0
    for i in range (n):
        first_index=i
        second_value=sum-arr[first_index]
        for j in range(i+1,n):
            if(arr[j]==second_value):
                second_index=j
                print("[",first_index,",",second_index,"]")
                break


arr = list(map(int, input("Enter the array: ").split()))
n=len(arr)
sum=int(input("Enter the value: "))
indexs(arr,n,sum)

