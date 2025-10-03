# get user's age and take that from current year to get birthyear
import datetime
from math import floor

now = datetime.datetime.now()
year = now.year
age = floor(float(input("How old are you? ")))
birthyear = year - age
print(f"You were born in {birthyear}!")
age += 3
print(f"you'll be {age} in 3 years.")