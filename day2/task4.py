x= int(input("enter number : "))
mario_pyr=[]
for i in range(1,x+1):  
    row=[]

    row.append(" "* (x-i)+"*" *i)
    mario_pyr.append(row)

for row in mario_pyr:
    print(row)
