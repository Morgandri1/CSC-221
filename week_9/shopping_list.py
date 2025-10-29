def main(l: list):
    i = input("What do you need to buy? ('break' to exit) ")
    if i != "break":
        l.append(i)
        return main(l)
    else:
        print(f"Your list has {len(l)} items:\n{',\n'.join(l)}")
        
main([])