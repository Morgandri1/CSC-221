# asks for a number, repeats until a specific number is entered

DESIRED = 27

while True:
    number = int(input("Enter a number: "))
    if number == DESIRED:
        print("Congratulations!")
        break
    else:
        print("Try again!")