from main2 import Sorting
x=True
y=True

while(x):
    try:
        arr = list(map(int, input("Enter the array: ").split()))
        n = len(arr)
        x=False

    except:
        print("Enter array of integers! ")

while(y):
    try:
        target=int(input("Enter the target number: "))
        print(Sorting(arr, n, target))
        y=False
    except:
        print("Enter an integer target within range")

