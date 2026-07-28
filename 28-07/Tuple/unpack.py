# extract the values back into variables. This is called "unpacking"

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

x = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *blue, red) = x

print(green)
print(*blue)
print(red)

# Loop and join methods are same as list 

# multiply tiple 
x = (1, 2, 3)
y = x*2
print(y)