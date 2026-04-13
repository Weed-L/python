start = int(input("Starting point: "))
end = int(input("Ending point: "))
increment = int(input("Increment by: "))

for i in range(start, end + 1, increment):
    print(i, end=" ")