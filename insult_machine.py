import insult_machine_util as im 

def main():
    print('TESTING: welcome()')
    im.welcome()

    print()
    
    print('TESTING: show_all_insults()')
    im.show_all_insults()
    
    print()
    
    print('TESTING: one_insult()')
    im.one_insult()

    print()
    
    print('TESTING: two_insults()')
    im.two_insults()

    print()

    print('TESTING: insult_specific_name(name)')
    name = input('What is your name? ')
    im.insult_specific_name(name)

    print()

    print('TESTING: insult_x_number_of_insults(num)')
    num = int(input('Enter number of insults: '))
    im.insult_x_number_of_insults(num)

    print()

    print('TESTING: goodbye()')
    im.goodbye()







if __name__ == "__main__":
    main()