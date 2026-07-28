listitems = ["apple", "banana", "cherry", "date", "elderberry" ]
listitems1 = ["dog", 1 , True, 3.14, "cat"]
print(listitems)
print(listitems1)
print(len(listitems)) # 5
print(type(listitems)) # <class 'list'>

thislist = list(("apple", "banana", "cherry"))
print(thislist) # ['apple', 'banana', 'cherry']

print(thislist[1]) # banana
print(thislist[-1]) # cherry
print(thislist[0:2]) # ['apple', 'banana']
print(thislist[:2]) # ['apple', 'banana']
print(thislist[1:]) # ['banana', 'cherry']
print(thislist[-2:]) # ['banana', 'cherry']

# To Add items
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry']

thislist[1:2] = ["watermelon", "kiwi"]
print(thislist) # ['apple', 'watermelon', 'kiwi', 'cherry']

thislist.insert(2, "orange")
print(thislist) # ['apple', 'watermelon', 'orange', 'kiwi', 'cherry']

thislist.append("mango")
print(thislist) # ['apple', 'watermelon', 'orange', 'kiwi', 'cherry', 'mango']

troplist = ["apple", "banana", "cherry"]
thislist.extend(troplist)
print(thislist) # ['apple', 'watermelon', 'orange', 'kiwi', 'cherry', 'mango', 'apple', 'banana', 'cherry']

troptuple = ("kiwi", "orange")
thislist.extend(troptuple)
print(thislist) # ['apple', 'watermelon', 'orange', 'kiwi', 'cherry', 'mango']

# To remove items 
thislist.remove("kiwi")
print(thislist) # ['apple', 'watermelon', 'orange', 'cherry', 'mango', 'apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist.pop()
print(thislist) # ['apple', 'watermelon', 'orange', 'cherry', 'mango', 'apple', 'banana', 'cherry', 'kiwi']

thislist.pop(1)
print(thislist) # ['apple', 'orange', 'cherry', 'mango', 'apple', 'banana', 'cherry', 'kiwi'] 

del thislist[0]
print(thislist) # ['orange', 'cherry', 'mango', 'apple', 'banana', 'cherry', 'kiwi']

# Empty the list
thislist.clear()
print(thislist) # []

# delete the list completely
del thislist
#print(thislist) # NameError: name 'thislist' is not defined