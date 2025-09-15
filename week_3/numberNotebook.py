def get_age() -> int:
    age_str = input("How old are you?\n")
    try:
        return int(age_str)
    except ValueError:
        print("not a valid integer!")
        return get_age() # recurse until valid int is passed

# get user age 
age = get_age()
# get new age by adding 15 to age
new_age = age + 15
# print a message about how old user is 
print(f"You will be {new_age} years old in 15 years.")
print(f"Your brother (who's a third of your age) will be {new_age/3} in 15 years.")