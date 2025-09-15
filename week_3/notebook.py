from datetime import datetime
days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print("Good Morning, it is Wednesday!")
now = datetime.now()
# if its before 12, "Morning", if its before 6pm, "Afternoon", else "evening"
tod = "Morning" if now.hour < 12 else "Afternoon" if now.hour < 18 else "Evening"
# datetime uses non-iso format by default
print(f"Good {tod}, it is {days_of_week[now.weekday()]}!") 