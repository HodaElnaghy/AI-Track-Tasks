def mean_value (arr):
    sum=0
    for i in range (len(arr)):
        sum+=arr[i]

    return sum / len(arr)
def standard_deviation_variance(arr):

    Mean = mean_value(arr)
    Variance=0
    for i in range(len(arr)):
        Variance += pow((arr[i]-Mean),2)
    Variance/=len(arr)
    Standard_Deviation=pow(Variance,0.5)
    return "Variance: ",Variance,"Standard Deviation: ",Standard_Deviation



def median_value(arr):
    arr.sort()
    if len(arr)%2==0:
        return (arr[int(len(arr)/2)]+arr[int(len(arr)/2-1)])/2
    else:
        return arr[(len(arr)//2 )]
def five_values(arr):
    arr.sort()
    minimum=min(arr)
    maximum=max(arr)
    q2 = median_value(arr)
    if len(arr)%2==0:
        q1=median_value(arr[:len(arr)//2])
        q3=median_value(arr[len(arr)//2:])
    else:
        q1 = median_value(arr[:len(arr) // 2])
        q3 = median_value(arr[len(arr) // 2+1:])
    Range=maximum-minimum
    IRQ=q3-q1


    return "min: ",minimum,"max: ",maximum,"Q1: ",q1, "Q2: ",q2,"Q3",q3,"Range: ",Range,"IRQ: ",IRQ




arr = list(map(int, input("Enter the array: ").split()))
print(five_values(arr))
print(standard_deviation_variance(arr))
