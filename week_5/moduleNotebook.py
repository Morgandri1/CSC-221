import math
import random
from module import prompt

name = prompt("What is your name?")
chars = list(name)
char_len = len(chars)

def guess_fav_number():
    fav = random.randint(0,100)
    answer = prompt(f"Is your favorite number {fav}?")
    if answer.lower() == "yes":
        return print(f"That's great! The (rough) square root of that number is {math.floor(math.sqrt(fav))}")
    return guess_fav_number() # recurse until user answers yes

print(f"Your name is {name} and it has {char_len} characters.")
guess_fav_number()

base = 64
print(f"The base is {base}")
print(f"The square root of {base} is {math.sqrt(base)}")
print(f"The cube root of {base} is {math.pow(base, 1/3)}")
print(f"The fourth root of {base} is {math.pow(base, 1/4)}")
print(f"Log base 8 of {base} is {math.log(base, 8)}")
print(f"a random integer between 1-10 is {random.randint(1,10)}")
print(f"a random float between 0-1 is {random.uniform(0,1)}") # could also just use rand.random()