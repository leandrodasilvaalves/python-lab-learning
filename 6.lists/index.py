mylist = ["apple", "banana", "cherry", "organge", "kiwi", "melon", "mango"]
print(mylist)

print(len(mylist))
print(type(mylist))

print(mylist[1])
print(mylist[-1])

print(mylist[2:5])
print(mylist[:4]) # até antes do item 4
print(mylist[2:]) # a partir do item 2
print(mylist[-4:-1])
print("mango" in mylist)

mylist[1]="watermelon"
print(mylist)

mylist[1:3] = ["blackcurrant", "strawberry"]
print(mylist)

mylist[1:3] = ["aaaaa"]
print(mylist)

mylist.append("bbbbb")
print(mylist)

mylist.insert(1, "cccc")
print(mylist)