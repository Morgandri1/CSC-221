import random as rand

def roll():
    return [
        rand.randint(1,7), 
        rand.randint(1,7), 
        rand.randint(1,7)
    ]

def get_bal():
    try:
        return int(input("Enter your balance: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_bal()

rewards = {
    "3": 30,
    "2": 5,
    "1": 2,
    "0": -1
}

def main(bal: int, max_bal: int, rn: int):
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
    else: 
        won = rewards[str(sevens)]
    bal += won
    print(f"You rolled {rolls[0]}, {rolls[1]}, and {rolls[2]}", end=" ")
    if sevens > 0: 
        print(f"which is {sevens} seven!", end=" ")
    if 3 > sevens > 0:
        print(f"~~~ - Lucky Seven{'s' if sevens > 1 else ""} - ~~~ You win ${won}!", end=" ")
    elif sevens == 3:
        print(f"@@@ - JACKPOT! - @@@ You win ${won}!", end=" ")
    if won == 0 and ones != 3:
        print("You lose $1!", end=" ")
    if bal > 0:
        print(f"Your new balance: ${bal}.")
        return main(bal,max_bal,rn)
    else: 
        print("which is tripple ones! XXX - Triclops caught you - XXX YOU LOSE EVERYTHING!")
    print(f"Sorry, you're all out of money. it took you {rn} rolls, and your highest balance was {max_bal}")
    
b = get_bal()
main(b,b,1)