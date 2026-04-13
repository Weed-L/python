PASSWORD = "tooManySecrets"
guess = ""

while guess != PASSWORD:
    guess = input("Enter password: ")
    if guess != PASSWORD:
        print("\nPassword does not match.")

print("\nAccess granted.")