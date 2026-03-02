def main():
    answer = input("Would you like a compliment? ")
    compliment_generator(answer)

def compliment_generator(answer):
    if (answer == 'yes'):
        print("You have wonderful eyes.")
    else:
        print("No compliment for you!")
    print("Thank you for playing.")

main()