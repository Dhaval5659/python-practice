# selection methods are same as list

#Update Tuple 
# to update we have to convert it in to list 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
 
print(thistuple)

y = ("orange",)
thistuple += y
print(thistuple)

a = list(thistuple)
a.remove("orange")
thistuple=tuple(a)
print(thistuple)

# del thistuple  -> to delete tuple

