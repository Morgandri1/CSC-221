import random

TX_FEE = random.randrange(0,51)
WELCOME_MESSAGE = f"""
**************************************
Welcome to Morgan's virtual coinstar!
Our current transaction fee is {TX_FEE}%
Let us know how many of each coin you have and we'll count it for you!
**************************************\n
"""

def main():
    print(WELCOME_MESSAGE)
    p = int(input("How many Pennies do you have? "))
    n = int(input("How many Nickels do you have? "))
    d = int(input("How many Dimes do you have? "))
    q = int(input("How many Quarters do you have? "))
    total = calculate_total_dollars(p,n,d,q)
    fee = calculate_tx_fee(total)
    print(f"""
--------------------------------------
Below are the results of our coin count:
You have {p+n+d+q}, which is ${total:.2f}!
Now I will compute my {TX_FEE}% count fee:
My {TX_FEE}% counting fee is ${fee:.2f}, leaving you with ${(total - fee):.2f}
--------------------------------------

*******************************************
Thanks for using Morgan's Virtual Coinstar!
Built with ❤️ by Morgan Metz
*******************************************
    """) # python's "f-string" operator allows you to automatically truncate floats
    
def calculate_total_dollars(p,n,d,q) -> float:
    """
    Calculate the value of coins in dollars
    \np - Pennies
    \nn - Nickels
    \nd - Dimes
    \nq - Quarters
    """
    total = 0
    total += p / 100 # 100 pennies/dollar
    total += n / 20 # 20 nickels/dollar
    total += d / 10 # 10 dimes/dollar
    total += q / 4 # 4 quarters/dollar
    return total
    
def calculate_tx_fee(total: float) -> float:
    """
    Calculates a transaction fee
    \nwe're instructed to do 0-50%, 
    although that's crazy high, 
    i'll follow through for the grade :)
    \nReturns: amount (in dollars) to subtract total by
    """
    return total * (TX_FEE / 100)
    
main()