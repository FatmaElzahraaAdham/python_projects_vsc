def multiplacation(x):
    for i in range(1,x+1):
        for j in range (1,i+1):
            print(f"{i}*{j}={i*j}")

def mul_list(y):
    y= int(input("enter number : "))
    mul=[]
    row=[]
    for i in range(1,y+1):
        for j in range (1,i+1):
            z=i*j
            row.append(z)

        mul.append(row)
        row=[]

    print(mul)

x= int(input("enter number for multiply : "))
multiplacation(x)
mul_list(x)
