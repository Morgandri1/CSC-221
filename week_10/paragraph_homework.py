i: list[str] = []
print("Enter a paragraph with at least three sentences. Use an empty line to finish up.")
stdin: str = input(">>> ")
while stdin != "":
    i.append(stdin)
    stdin = input(">>> ")
all = " ".join(i)

words = all.split()
sentences = [s.strip().removesuffix(".") for s in all.split(".")]
lines = i

print("\nYour entry:\n", all.strip())
print(f"\n{len(words)} Words:\n{'\n'.join(words)}") # Number of words followed by a list seperated by newline
print(f"\n{len(sentences)} Sentences:\n{'\n'.join(sentences)}")
print(f"\n{len(list(''.join(words)))} Characters excluding spaces")
print(f"{len(all)} Characters including newlines and spaces")
ri = input("\nEnter a character to replace in your paragraph: ")
ro = input(f"Enter the charachter you'd like to replace {ri} with: ")
print(f"\nHere is your paragraph after replacing all occurences of {ri} with {ro}:")
print(all.replace(ri, ro))