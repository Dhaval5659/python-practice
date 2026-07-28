thisdict = {
 "brand" : "Ford",
 "model" : "Mustang",
 "year" : 1964,
 "year" : 2000,          # no duplicate key
 "colors" : ["red", "white", "blue"]
}

print(thisdict)

print(thisdict["brand"])

newdict = dict(name = "dhaval", age=75, blood = "+O")
print(newdict)

# for value only
x = newdict.get("blood")
print(x)

# show all keys
x = thisdict.keys()
print(x)

# add new key: value pair or change the value
thisdict["colors"] = "black"
print(thisdict)

thisdict.update({"year": 2020})
print(thisdict)

# shows value only
y = thisdict.values()
print(y)

y = thisdict.items()
print(y)

# Remove items
thisdict.pop("model")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["brand"]
print(thisdict)

thisdict.clear()
print(thisdict)
