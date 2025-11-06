import math as m

def get_circle_area(r: float) -> float:
    """Calculates the area of a circle from the radius"""
    return m.pi * (r**2)
    
for i in range(3,6):
    print(f"a circle with {i}-inch radius has an area of {get_circle_area(i):.2f} square inches")
    
def first_last_letter(string: str) -> tuple[str, str]:
    return string[0], string[-1]
    
def create_acronym(sentence: str) -> str:
    words = sentence.split()
    first_letters = [w[0].upper() for w in words]
    return "".join(first_letters)
    
sentence = "Northrop Grumman Corporation"
print(f"An acronym for {sentence} would be {create_acronym(sentence)}")