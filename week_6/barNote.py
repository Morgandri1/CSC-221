age = int(input("Enter your age: "))

if age >= 21:
    print("Come on in!")
else:
    guardian = input("Are you with a guardian? (yes/no): ")
    if guardian.lower() in ["yes", "y"]:
        print("Come on in!")
    else:
        print("Sorry, you're too young.")
print("Thanks for using bouncerbot")

# Cleaner and only uses one level of Indentation

def bouncerbot():
    age = int(input("Enter your age: "))
    
    if age >= 21:
        return print("Come on in!") # early return stops execution in place
    guardian = input("Are you with a guardian? (yes/no): ")
    if guardian.lower() in ["yes", "y"] and int(input("How old is your guardian? ")) >= 21:
        print("Come on in!")
    else:
        print("Sorry, you're too young.")