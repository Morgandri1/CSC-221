num1 = 113
num2 = 8

quotient = num1 / num2
print(quotient)

int_quotient = num1 // num2
remanider = num1 & num2
print(int_quotient)

slices = 8
num_people = 3
num_slices = slices // num_people
left_over = slices % num_people

print(f"There are {num_slices} for each people." )
print(f"There are {left_over} left over.")