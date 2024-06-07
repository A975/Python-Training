import os

# r = Read
# a = Append
# w = Write
# x= Create

#Read - error i it doesn't exist

f = open("names.txt")
#print(f.read()
# #print(f.read(4)))

print(f.readline())
print(f.readline())

for line in f:

    print(line)


f.close()

# Append - creates the file of it doesn't exist

f = open("names.txt","a")
f.write("Neil")
f.close()


f = open("names.txt")
print(f.read())
f.close()

#Write (overwrite)
f = open("names.txt", "w")
f.write("I delete all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#Opens a file for writing creates a file if t does not exist

f = open("name_list.txt","w")

if not os.path.exists("dave.txt"):

    f = open("dave.txt","x")
    f.close()

#Delete a file

#avoid an error if it doesn't exist
if os.path.exists("dave.txt"):

    os.remove("dave.txt")

else:

    print("The file u wish to delete does not exist")

with open("more_names.txt") as f:

    content = f.read()

with open("names.txt","w") as f:

    f.write(content)

