SECRET_NUMBER = 33
tries = 0
guess = None

while guess != SECRET_NUMBER:
    guess = int(input("Guess a number: "))
    tries += 1

print(f"You guessed in {tries} tries.")