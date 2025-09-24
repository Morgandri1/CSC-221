num1 = 16
num2 = 8

quotient = num1 / num2
print(f"The quotient of {num1} and {num2} is {quotient}")

int_quotient = num1 // num2
print(f"The integer quotient of {num1} and {num2} is {int_quotient}")

remainder = num1 % num2
print(f"The remainder of {num1} divided by {num2} is {remainder}")

FOOT = 12
inches = int(input("Enter the number of inches: "))

feet = inches // FOOT
print(f"The number of feet is {feet}")
inches = inches % FOOT
print(f"The number of inches is {inches}")

yards = feet // 3
print(f"The number of yards is {yards}")

miles = yards // 1760
print(f"The number of miles is {miles}")
