filename = input("File name? ")
entry = input("Word to add? ")

# add entry to file
with open(filename, "a") as file:
    file.write(entry + "\n")

print()

# read and display file contents
with open(filename, "r") as file:
    for line in file:
        print(line.strip())