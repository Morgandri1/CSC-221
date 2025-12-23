def human_years_to_dog_years(n: float = 1) -> float:
    "Calculates relative dog 'age' by their relative aging speed to humans"
    return n * 7

print(f"My dog was born in 2017, so he's {human_years_to_dog_years(2025-2017)} years old!")
print(human_years_to_dog_years.__doc__) # print docstring
print(human_years_to_dog_years.__annotations__) # print type annotations
print(human_years_to_dog_years.__code__) # prints function code
print(human_years_to_dog_years.__defaults__) # prints default parameter(s)
print(human_years_to_dog_years.__name__) # prints function name