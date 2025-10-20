from random import randint

balance = float(50)

def casino(user_bet, balance) -> float:
    balance -= user_bet
    roll = randint(1, 6)
    prize = (user_bet * 2)
    if 4 <= roll <= 6:
        print(f"You win! Your new balance is {balance + prize:.2f}.")
    else:
        print("You lose!")
        return balance
    if input("Would you like to play double or nothing? y/N ").lower() == "y":
        return casino(prize, balance + prize)
    else:
        return balance + prize

while balance > 0:
    user_bet = float(input(f"How much would you like to bet? (0 to leave, max {balance:.2f}) "))
    if user_bet > balance:
        print("You don't have enough money!")
        continue
    elif user_bet <= 0:
        print("Goodbye")
        break
    balance = casino(user_bet, balance)