mylist = ["banana","cherry","apple"]
print(mylist)

mylist2 = [5,True, "apple"]
print(mylist2)


if "apple" in mylist:

    print(mylist)
 
item = mylist[-2]
print(item)

for x in mylist:

    print(x)

mylist.insert(1,"blueberry")
print(mylist)

#remove element from mylist from the last position
item = mylist.pop()
print(item)
print(mylist)