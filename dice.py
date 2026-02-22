import random

def main():
    seed = float(input("Enter a seed for the random number generation: "))
    roll_die(seed)

def roll_die (seed):
    random.seed(seed)

    die_roll_one = random.randint(1, 6)
    die_roll_two = random.randint(1, 6)

    print(f"Die roll one is {die_roll_one}")
    print(f"Die roll two is {die_roll_two}")

main()
