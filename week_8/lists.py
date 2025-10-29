my_list = [2, 5, "five", 80]

shopping_list = ["apple", "banana", "orange", "soap"]
print(f"My entire list: {shopping_list}")
print(f"first element: {shopping_list[0]}") # indices start at 0
print(f"The rest is {", ".join(shopping_list[1:])}") # second on, joined with a space and comma
print(f"The second and third elements are {", ".join(shopping_list[1:4])}") # slice indices are exclusive end

my_favorite_bikes = ["R6", "R1", "S1k", "Busa"]
print(f"My favorite bikes are {', '.join(my_favorite_bikes)}")
print(f"My favorite bike is the {my_favorite_bikes[0]}")
print(f"My least favorite bike of my favorites is {my_favorite_bikes[-1]}") # negating indices allows you to index from back. -1 is last, -2 is second-last, etc.

my_favorite_bikes.append("ZX-10")
my_favorite_bikes.append("YZM1R")
print(f"My other favorite bikes are {', '.join(my_favorite_bikes[-2:])}")
print(f"But, the {my_favorite_bikes.pop()} isn't publicly availible, so i'll remove it.")
print(f"The corrected list is {', '.join(my_favorite_bikes)}")
my_favorite_bikes.append(input("What's a bike you'd like to add to the list? "))
print(f"Great! so you like the {my_favorite_bikes[-1]}")
print(f"That makes the list {', '.join(my_favorite_bikes)}")

shopping_list.extend(my_favorite_bikes[0:2])
print("Now i'm going to make a things i plan to get while i'm out. I'm feeling pretty lavish so i think i'll pick up a couple bikes while i'm out.")
print(f"I think i'll need...\n{',\n'.join(shopping_list)}")

# min(my_list) >> 2
# max(my_list) >> 80
# sum([1,2,3]) >> 6
# my_favorite_bikes.index("R6") >> 0
# my_favorite_bikes.count("R1") >> 1