# Get user's favorite animal and number
import math
animal = input("What is your favorite animal? ")
num = float(input("What is your favorite number? "))

type(animal) # <class 'str'>
type(num) # <class 'float'>

print(f"You'll be sent {math.floor(num)} {animal}{"s" if num > 1 else ""}")