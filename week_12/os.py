from os import getcwd, walk, chdir, path, stat, mkdir

print(getcwd())

for t in walk(getcwd()):
    print(t)

chdir(path.dirname(path.abspath(__file__)))
fileinfo = stat("grades.csv")
print(fileinfo)

mkdir("new_directory")
chdir("new_directory")

with open("new_file.txt", "w") as f:
    f.write("Hello, World!\ntest...")
    f.close()

with open("new_file.txt", "a") as f:
    f.write("\nThis is a new line.")

with open("new_file.txt", "r") as f:
    print(f.read())
