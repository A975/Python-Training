value = 1

while value <= 10:

    value += 1

    if value == 5:
        continue
        print(value)
    else:
        print("Value is now equal to "+str(value))


names = ["Dave","Sara","John"]

for x in names:
    print(x)

for x in "Mississippi":
    print(x)


for x in names:
    if x == "Sara":
        break
    print(x)


for x in names:
    if x == "Sara":
        continue
    print(x)

for x in range(4):
    print(x)


for x in range(0,100,5):

    print(x)

else:
    
    print("Glad that's over!")

names = ["Dave","Sara","John"]
actions = ["codes","eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")

