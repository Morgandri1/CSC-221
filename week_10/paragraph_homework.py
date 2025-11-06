i: list[str] = []
print("Enter a paragraph with at least three sentences. Use an empty line to finish up.")
stdin = input(">>> ")
while stdin != "":
    i.append(stdin)
    stdin = input(">>> ")
all = "\n".join(i)

words = all.split()
sentences = all.split(".")
lines = i

print("Your entry:\n", all)
print(f"{len(words)} Words:\n{'\n'.join(words)}") # Number of words followed by a list seperated by newline
print(f"{len(sentences)} Sentences:\n{'.\n'.join(sentences)}")
print(f"{len(list(''.join(words)))} Characters excluding spaces")
print(f"{len(all)} Characters including newlines and spaces")
ri = input("Enter a character to replace in your paragraph: ")
ro = input(f"Enter the charachter you'd like to replace {ri} with: ")
print(f"Here is your paragraph after replacing all occurences of {ri} with {ro}:")
print(all.replace(ri, ro))