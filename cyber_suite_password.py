import random
import string

def main():
    seed = int(input("Enter a seed for the random number generation: "))
    generate_password(seed)

def generate_password(seed):
     
    random.seed(seed)
    
    special_chars = "!@#$&(),-_"
    
    password = (
        random.choice(special_chars) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.ascii_uppercase) +
        random.choice(string.digits) +
        random.choice(string.digits) +
        random.choice(special_chars) 
    )
    
    print("Your random password is:")
    print(password)

main()