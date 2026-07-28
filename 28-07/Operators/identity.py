x = ["banana", "apple", "mango"]
y = ["banana", "apple", "mango"]
z = x

print(x is y) # False (x and y are different objects in memory) 
print(x is z) # True (z is the same object as x)
print (x == y) # True (x and y have the same content)