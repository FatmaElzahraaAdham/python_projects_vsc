x = input("enter string: ")
vowels="aeiouAEIOU"
count =0
for i in x:
    if i in vowels:
        count+=1
print(f"num of vowels = {count}")