import math as m

def price_per_inch(diameter: float, price: float) -> float:
    area = m.pi * ((diameter/2) ** 2)
    return price / area
    
for (d,p) in [(10, 9), (14, 14), (20, 24)]:
    print(f'Price per square inch of a {d}" pizza is ${price_per_inch(d,p):.2f}')