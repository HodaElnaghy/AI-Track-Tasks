def HighestRange(dict):
    Highest=0
    temp=0
    Keys=''
    for k in dict.keys():
        n=len(dict[k])
        dict[k].sort()
        temp=dict[k][n-1]-dict[k][0]
        if (temp>Highest):
            Highest=temp
            keys=k
    return (keys)

dict={
    "A":[20,30,100,49] ,
    "B":[00,199,201,29] ,
    "C":[40,90,69,18]
}


print(HighestRange(dict))