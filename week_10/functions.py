import math as m

DOG_AGE_FACTOR = 7

def get_circle_area(r: float) -> float:
    """Calculates the area of a circle from the radius"""
    return m.pi * (r**2)
    
def first_last_letter(string: str) -> tuple[str, str]:
    return string[0], string[-1]
    
def create_acronym(sentence: str) -> str:
    words = sentence.split()
    first_letters = [w[0].upper() for w in words]
    return "".join(first_letters)
    
def add_five(n: float) -> float:
    return n + 5
    
def double_difference(a: float,b: float) -> float:
   return 2 * (a - b) 
   
def add(*n: float) -> float:
    return sum(n)
    
def main():
    # test create_acronym function
    sentence = "Northrop Grumman Corporation"
    print(f"An acronym for {sentence} would be {create_acronym(sentence)}")
    # test get_circle_area function
    for i in range(3,6):
        print(f"a circle with {i}-inch radius has an area of {get_circle_area(i):.2f} square inches")
        
if __name__ == "__main__": # prevent logic from running when module is imported 
    main()