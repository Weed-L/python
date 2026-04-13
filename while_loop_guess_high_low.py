SECRET_NUMBER = 33
tries = 0
guess = None

while guess != SECRET_NUMBER:
    guess = int(input("Guess a number: "))
    tries += 1
    if guess < SECRET_NUMBER:
        print("Your guess is too low.\n")
    elif guess > SECRET_NUMBER:
        print("Your guess is too high.\n")

print(f"You guessed in {tries} tries.")