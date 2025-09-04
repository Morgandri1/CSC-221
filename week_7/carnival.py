from random import randrange

WELCOME_MESSAGE = "******Welcome to the Carnival TicketMaster!******"
EXIT_MESSAGE = "******Thank you for your purchase! Enjoy the carnival******"

def main():
    print(WELCOME_MESSAGE)
    # default all inputs to 0 if user skips prompt
    a = int(input("How many adult tickets do you want to purchase? (18+) >> ") or 0)
    s = int(input("How many of the adults are older than 60? >> ") or 0)
    k = int(input("How many children tickets do you want to purchase? (< 17) >> ") or 0)
    t = int(input("How many of the children are under 5? >> ") or 0) 
    price = calculate_cost(
        a - s, # subtract senior tickets from regular adult pricing
        s,
        k - t, # subtract toddler tickets from regular kid pricing
        t
    )
    (percent, discount) = calculate_discount(price)
    print(f"Your total ticket price is ${price:.2f}")
    if discount > 0: 
        print(f"Wait! You qualify for a large purchse discount of {percent}% (${discount:.2f})")
        print(f"Your new total ticket purchase with discount is {(price - discount):.2f}!")
    print(EXIT_MESSAGE)

def calculate_cost(a,s,k,t) -> float:
    """
    ### Calculates the total cost of carnival tickets.
    #### Params
    - a: Number of adults
    - s: Number of seniors
    - k: Number of kids
    - t: Number of todlers (< 5 y/o)
    #### Returns
    - cost of n tickets as a float 
    """
    total = 0
    total += a * 11
    total += s * 5.50
    total += k * 7
    total += t * 1.50
    return total
    
def calculate_discount(total: float):
    """
    if the total cost is > 45, 
    calculate a discount between 1-15%. 
    Returns both the discount % and amount off total
    """
    discount = randrange(1,16)
    if total >= 45:
        return (discount,total * (discount / 100))
    return (0,0)
    
main() # made with ❤️ by Morgan Metz