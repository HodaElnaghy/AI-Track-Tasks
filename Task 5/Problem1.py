import math
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return  arr

def mean_value (arr):
    sum=0
    for i in range (len(arr)):
        sum+=arr[i]
    return sum/len(arr)

def median_value(arr):
    insertionSort(arr)
    if len(arr)%2==0:
        return (arr[int(len(arr)/2)]+arr[int(len(arr)/2-1)])/2
    else:
        return arr[math.floor(len(arr)/2 )]


from collections import Counter
def my_mode(arr):
    insertionSort(arr)
    c = Counter(arr)
    check = c[arr[0]]
    #checking if all the array have the same counting numbers
    for i in range (1,len(arr)):
        if check != c[arr[i]]:
            break
        if i==len(arr)-1:
            return "no mode exists"

    return [k for k, v in c.items() if v == c.most_common(1)[0][1]] #msh fahma el satr da

#Another solution
def mode_value(arr):
    modes=[]
    insertionSort(arr)
    counting = [0]*(max(arr)+1)
    for i in range (len(arr)):
        counting[arr[i]]+=1
    # checking if there is no mode
    if 0 in counting:
        if len(set(counting))==2:
            return "no mode exists"
    elif len(set(counting))==1:
            return "no mode exists"
    maximum=max(counting)
    for i in range (len(counting)):
        if counting[i]==maximum:
            modes.append(i)
    return modes

arr = list(map(int, input("Enter the array: ").split()))
