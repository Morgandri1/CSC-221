import libFile as f

name = input("Enter the file name: ")
content = input("Enter the content to write: ")
opt = input("Enter the write mode; 'w' to overwrite or 'a' to append: ")
if opt not in ["w", "a"]:
    print("Invalid write mode")
else:
    if opt == 'w':
        f.write(name, content)
    elif opt == 'a':
        f.write(name, "\n" + content, mode='a')
        print(f.read(name))

print("Done!")