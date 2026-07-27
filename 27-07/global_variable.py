x = "awesome"

def myfunc():
 global x
 x = "excellent"
 print("python" + " " + x)

print("python", x) # awesome
myfunc();          # excelent (updated)

print("python", x) #excellent (global after func)

