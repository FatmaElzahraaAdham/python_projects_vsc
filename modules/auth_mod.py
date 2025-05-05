list=[{"name":"fatma","pass":"123"},{"name":"adham","pass":"456"}]
def authorization(user):
     
    for i in range(len(list)):
        if user==list[i]["name"]:
            userpass=input("please enter password : ")
            if userpass==list[i]["pass"]:
                print("authorized")
                break
            else:
                print("not authorized")
                break
    else:
        print("username is wrong")

            
username=input("enter your name : ")
authorization(username)
    

