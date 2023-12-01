import math
from math import sqrt 

print("welcome to the pythagoras solver")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("Assuming that the sides are a/b or side c (hypotenuse) ")
calculation = input("Which side do you want to calculate a, b or c? ")
if calculation == 'c':
  a = float(input("What is side a "))
  b = float(input("What is side b "))
  c = sqrt(a * a + b * b )
  print("The length of side c is  ")
  print(c)
elif calculation == 'a':
  a = float(input("What is side b "))
  b = float(input("What is side c "))
  c = sqrt(a * a + b * b )
  print("The length of side a is  ")
  print(a)
elif calculation == 'b':
  a = float(input("What is side a "))
  b = float(input("What is side c "))
  c = sqrt(a * a + b * b )
  print("The length of side b is  ")
  print(b)