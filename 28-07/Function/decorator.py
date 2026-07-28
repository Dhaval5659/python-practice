def fun(x):
 def inner():
  return x().upper()
 return inner

def greeting(x):
 def myinner():
  return "Hello " + x() + " Have a good day!"
 return myinner

@greeting
@fun                         # this calls upper one
def name():
 return "Dhaval"

print(name())


