import random

def main():
    print("===== Coin Flipper =====")
    number = coin_flipper()
    if number >= 51:
        print("Tails")
    else:
        print("Heads")

def coin_flipper():
    number = random.randint(1, 100)
    return number

main()