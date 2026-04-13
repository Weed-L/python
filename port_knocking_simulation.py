print("===== PORT KNOCKING FIREWALL SIMULATOR =====")
print("This firewall requires a specific sequence of port connections.")
print("You have 3 attempts to find the correct sequence.")
print("(Hint: Enter ports as integers, one at a time)\n")

SECRET_SEQUENCE = [2222, 3333, 4444, 5555]

max_attempts = 3
attempt = 1

while attempt <= max_attempts:
    print(f"Attempt {attempt} of {max_attempts}:")
    print("Enter your port knock sequence. Enter 0 when finished.")

    user_sequence = []

    while True:
        port = int(input("Enter port number: "))
        if port == 0:
            break
        user_sequence.append(port)

    print()

    if user_sequence == SECRET_SEQUENCE:
        print("FIREWALL RESPONSE: Connection accepted!")
        print("Correct port knocking sequence detected.")
        print("Firewall has opened port 22 for your connection.")
        break
    else:
        print("FIREWALL RESPONSE: Connection rejected!")

        if len(user_sequence) != len(SECRET_SEQUENCE):
            print(f"Your sequence had {len(user_sequence)} knocks, but the firewall expects {len(SECRET_SEQUENCE)}.")

        if attempt < max_attempts:
            print()

    attempt += 1