import random as rand

def roll():
    r1 = rand.randint(1,7)
    r2 = rand.randint(1,7)
    r3 = rand.randint(1,7)
    return r1, r2, r3

def get_bal():
    try:
        return int(input("Enter your balance: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_bal()

bal = get_bal()
rn = 0 # number of rolls
max_bal = bal

while bal > 0:
    if bal > max_bal:
        max_bal = bal
    rolls = roll()
    rn += 1
    sevens = 0
    ones = 0
    won = 0
    for r in rolls:
        if r == 7:
            sevens += 1
        if r == 1:
            ones += 1
    if ones == 3:
        bal = 0
    elif sevens == 3:
        won = 30
    elif sevens == 2:
        won = 5
    elif sevens == 1:
        won = 2
    else:
        bal += -1
    bal += won
    print(f"You rolled {rolls[0]}, {rolls[1]}, and {rolls[2]}", end=" ")
    if ones == 3:
        print("which is tripple ones! XXX - Triclops caught you - XXX YOU LOSE EVERYTHING!", end=" ")
        bal = 0
    elif sevens > 0: 
        print(f"which is {sevens} seven!", end=" ")
    if 3 > sevens > 0:
        print(f"~~~ - Lucky Seven{'s' if sevens > 1 else ""} - ~~~ You win ${won}!", end=" ")
    elif sevens == 3:
        print(f"@@@ - JACKPOT! - @@@ You win ${won}!", end=" ")
    if won == 0 and ones != 3:
        print("You lose $1!", end=" ")
    print(f"Your new balance: ${bal}.")
print(f"Sorry, you're all out of money. it took you {rn} rolls")