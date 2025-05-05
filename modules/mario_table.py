def normal_mario(x):
    
    for i in range(1,x+1):   
        print(" "* (x-i)+"*" *i)

def mario_list(x):

    mario_pyr=[]
    for i in range(1,x+1):  
        row=[]

        row.append(" "* (x-i)+"*" *i)
        mario_pyr.append(row)

    for row in mario_pyr:
        print(row)

x= int(input("enter number : "))
normal_mario(x)
mario_list(x)
       