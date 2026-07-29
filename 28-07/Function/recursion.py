def countdown(x):
 if x <= 0:
  print("Done!")
 else: 
  print(x)
  countdown(x-1)

countdown(5)

# Fibonacci 

def fibonacci(n):
 if n<= 1:
  return n
 else:
  return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

# with list 

def sumlist(numbers):
 if len(numbers) == 0:
  return 0
 else:
  return numbers[0] + sumlist(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sumlist(my_list))

# recursion deft limit is around 1000
import sys
print(sys.getrecursionlimit())
