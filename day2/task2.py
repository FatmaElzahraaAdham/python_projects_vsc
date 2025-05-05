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


