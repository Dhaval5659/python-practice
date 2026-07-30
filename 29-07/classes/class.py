class MyClass:
 x = 5

p1 = MyClass()
print(p1.x)
#-----------------------------------------------------------
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emli")
p2 = Person("Meet", 35)

print(p1.name, p1.age)
print(p2.name, p2.age)