thisset = {"apple", "banana", "cherry"}

for x in thisset:
 print(x)

print("banana" in thisset)
print("banana" not in thisset)

# add items

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
mylist = ["new", "old"]

thisset.update(tropical)
thisset.update(mylist)

print(thisset)

# to remove items
thisset.remove("mango")
print(thisset)

thisset.discard("old")
print(thisset)

# remove random item
thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

del thisset
#print(thisset)

