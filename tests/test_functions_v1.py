import random

print(random.randrange(1, 10))

x = "awesome!"

def myFunc():
    x = "fantabulous!"
    print("Python is " + x)

myFunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

