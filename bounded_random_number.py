import random

def main():
    seed = float(input("Enter a seed for the random number generation: "))
    print(bounded_random(seed))

def bounded_random(seed):
    random.seed(seed)
    return random.randint(1, 10)

main()