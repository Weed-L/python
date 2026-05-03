import random

# You need to add at least five more insults (for a total of at least six)
# Insert your insults into the strings in the list.
insults = [
    'You look like a bunch of rocks',
    'A',
    'B',
    'C',
    'D',
    'E'
]

def welcome():
    print('---------------------------------')
    print('Welcome to the Insulternator 3500')
    print('---------------------------------')
    print()  


def show_all_insults():
    print(insults)


def one_insult():
    print(random.choice(insults))

    
def two_insults():
    one_insult()
    one_insult()


def insult_specific_name(name):
    insult = random.choice(insults)
    print(f"{name}, here is your insult: {insult}")



def insult_x_number_of_insults(num):
    for _ in range(num):
        print(random.choice(insults))


def goodbye():
    print()
    print('---------------------------------------------')
    print('Thank you for playing the Insulternator 3500!')
    print('---------------------------------------------')   



