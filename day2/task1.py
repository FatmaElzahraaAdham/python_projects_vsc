arr=[]
print("please enter 5 numbers")
for i in range (5):
    x= int(input(f"enter item {i} in list : "))
    arr.append(x)
    
ascending = sorted(arr)
descending = sorted(arr, reverse=True)
print (f"their ascending order is {ascending}")
print (f"their descending order is {descending}")