channel = 100

if 1 < channel < 200: # always true as channel is a literal
    print("Channel is in HD")
elif 200 < channel <= 600:
    print("Channel is in 4k")
else: 
    print("Non existent channel number")