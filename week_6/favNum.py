if 3 == 1:
    print("3 is equal to 1") # unreachable

# use of two literals for comparison is uncommon and
# generally bad practice as it confuses control flow
if 3 > 1:
    print("3 is greater than 1") # always true

print("Anything outside a conditional block will run no matter what")

# get user's fav number 
fav_num = float(input("Enter your favorite number: ")) # just in case they're cheeky
difference = fav_num - 27
if difference < 0:
    difference = difference * -1

# if user's favorite number is also mine, let them know
if difference == 0:
    print("Your favorite number is the same as mine!")
elif 0 < difference < 5:
    print(f"Your favorite number is close to mine! only {difference} off")
else:
    print(f"{fav_num} is a great choice!")
