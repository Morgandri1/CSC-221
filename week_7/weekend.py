temp = float(input("What is the average tempurature for this weekend? (deg. fahrenheit) "))
sunny = input("Is it sunny outside? y/N ").lower() == "y"
if temp >= 65 and sunny:
    print("Go outside and get some sun!")
elif temp >= 65 and not sunny: # if warmer than 65º and not sunny outside
    print("Go outside and enjoy the weather!")
elif 32 < temp < 65 or sunny: # if warmer than 32º or sunny outside
    print("Go out and bundle up!")
else: # if colder than 32º and not sunny
    print("Stay inside and watch a movie!")
