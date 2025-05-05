list=[{"name":"fatma","pass":"123"},{"name":"adham","pass":"456"}]

username=input("enter your name : ")

for i in range(len(list)):
    if username==list[i]["name"]:
        userpass=input("please enter password : ")
        if userpass==list[i]["pass"]:
            print("authorized")
            break
        else:
            print("not authorized")
            break
else:
    print("username is wrong")

        

    

