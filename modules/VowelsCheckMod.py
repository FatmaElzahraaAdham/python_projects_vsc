def checkvowels (word):
    vowels="aeiouAEIOU"
    count =0
    for i in word:
        if i in vowels:
            count+=1
    return count

x = input("enter string: ")

print(f"num of vowels = {checkvowels(x)}")
    