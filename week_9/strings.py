string = input("Enter any string: ")
print(string)
print("Your string is " + str(len(string)) + " characters long")
print(f"First char of your string is {string[0]}")
print(f"The rest of your string is {string[1:]}")
rstr = string.replace("l", "r")
print("After replacing L with R, here is the new string:", rstr)
print(f"The original was '{string}'")

# finding char instances
long = "abracadabraalakazam"
print(long.find("a")) # first instance of a 

# read file 
path = "/Users/metatron/Documents/csc-221/week_9/file.txt"
path_parts = path.split("/")
user = path_parts[2] # Even though username is the second instance, because of the leading slash, it becomes index 2, with index 0 being "".
print("You must be", user + "!")
print(f"The windows version of your path would be C://users//{user}//{'//'.join(path_parts[3:])}")
print(f"Lets open the {path_parts[-1]} file and have some fun.")
with open(path, "r+") as f:
    print(f"Current file contents: \n{f.read()}")
    print("Adding a new line...")
    f.write("\nMy name is Morgan")
    f.close()

def letters(s: str | None = None):
    s = s or input("Enter a string longer than 5 characters, but less than 12: ")
    n = input("Now enter a number with three digits")
    if 5 >= len(s) >= 12: # validate s characters 
        print("Invalid string entry. Try again.")
        return letters()
    if len(n) != 3: # validate n digits
        print("Invalid number entry. Must be exactly 3 digits. Try again.")
        return letters(s)
    try: # verfiy that n is actually a number
        n = int(n.split(".")[0])
    except ValueError:
        print("You must enter a valid floating point number or integer.")
        return letters(s)
    print(f"The first instance of the letter a is at index {s.lower().find("a")}.")

letters()