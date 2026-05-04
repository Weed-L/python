filename = input("File name? ")

print()

# read and display file contents
with open(filename, "r") as file:
    for line in file:
        print(line.strip())

print()