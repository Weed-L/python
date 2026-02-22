import random

def main():
    seed = float(input("Enter a seed for the random number generation: "))
    print(generate_seeded_random_number(seed))

def generate_seeded_random_number(seed):
    random.seed(seed)
    return random.random()

main()