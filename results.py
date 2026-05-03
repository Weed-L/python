results = []

def mathenator2000():
    print("Welcome to the Mathenator2000")
    
    
    play_again = 'y'
    
    while play_again.lower() == 'y':
        print("\nPlease choose from the following menu:")
        print("  1. Compute area of a circle")
        print("  2. Compute area of a rectangle")
        
        choice = input("\nWhat is your choice? ")
        
        if choice == '1':
            radius = float(input("\nWhat is the radius of the circle? "))
            area = 3.14 * radius * radius
            result = f"The area of the circle is {area}"
            print(result)
            results.append(result)
        
        elif choice == '2':
            length = float(input("\nWhat is the length of the rectangle? "))
            width = float(input("What is the width of the rectangle? "))
            area = length * width
            result = f"The area of the rectangle is {area}"
            print(result)
            results.append(result)
        
        else:
            print("\nInvalid selection.")
        
        play_again = input("\nWould you like to play again (y/n)? ")
    
    print("\n-------------------------")
    print("A record of your results: ")
    print(results)
    print("\nThank you for using the Mathenator2000")

mathenator2000()