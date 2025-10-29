pet_names = ["Riley", "Meeko", "Pippin", "Merry", "Merry"]
user_input = input("What's your pet's name? ")
pet_names.append(user_input)
print(set(pet_names)) # Will remove duplicates
for pet in pet_names:
    if pet == "Riley":
        print("My dog, Riley")
    else:
        print(pet)