users = ['Dave','John','Sara']

pop1 = ['Dave', 42, True]

print(pop1)

emptylist = []

print("Dave" in users)

print(users[0])

print(users[-1])

print(users.index('Sara'))

print(users[0:2])

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(pop1))

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert','Jimmy'])
print(users)

users.extend(pop1)
print(users)

users.insert(0,"Bob")
print(users)

users[2:2] = ['Eddie','Alex']
print("********")
print(users)

users[1:3] = ['Robert','JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

#del data
print(pop1)

# users[1:2] = ['dave']
# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

nums = [4,42,78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse = True)
print(nums)

users[2:2] = ['Eddie','Alex']
print(users)

users[1:3] = ['Robert','JPJ']
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
# print(data)

#del pop1
pop1.clear()
print(pop1)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy.sort())
print(nums)

print(type(nums))

mylist = list([1,"Neil",True])
print(mylist)

# Tuples
mytuple = tuple(('Dave',42,True))

anothertuple = (1,4,2,8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey)  = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

