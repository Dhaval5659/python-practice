thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) # apple, banana, cherry

for i in range(len(thislist)):
  print(thislist[i]) # apple, banana, cherry

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# newlist = [x for x in fruits if "a" in x]

thislist.sort()
print(thislist)

x = [1,25,9,6,3,4,7,0]
x.sort()
print(x)

x.sort(reverse=True)
print(x)

x.reverse()
print(x)

#copy list

y = x[:]
print(y)

y = list(x)
print(y)

# join list

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list = list1 + list2
print(list)

# by loop

for x in list2:
  list1.append(x)

print(list1)

list1.extend(list2)
print(list1)

