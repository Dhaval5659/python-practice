def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)


def numbers(n):
    count = 1
    while count <= n:
     yield count
     count += 1

for num in numbers(5):
   print (num)


def larg_rang(n):
   for i in range(n):
      yield i

gen = larg_rang(10000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# fibbonacci

def fibbonacci():
   a, b = 0, 1
   while True:
      yield a
      a, b = b, a + b

gen = fibbonacci()
for _ in range(100):
   print(next(gen))