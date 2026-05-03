# FILE NAME - calc.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

########## ENTER YER CODE BELOW THIS LINE ##########
import calc_util

print('Welcome to the Calculator')
first_num = float(input('\nWhat is the first number? '))
second_num = float(input('What is the second number? '))
print('')
print('SUM = ', calc_util.add(first_num, second_num))
print('DIFFERENCE = ', calc_util.subtract(first_num, second_num))
print('PRODUCT = ', calc_util.multiply(first_num, second_num))
print('QUOTIENT = ', calc_util.divide(first_num, second_num))
print('')
print('Have a nice, mathy day.')








########### END YER CODE ABOVE THIS LINE ###########




########################################
#          SAMPLE OUTPUT
########################################

'''

Welcome to the Calculator

What is the first number? 10
What is the second number? 5

SUM =  15.0
DIFFERENCE =  5.0
PRODUCT =  50.0
QUOTIENT =  2.0

Have a nice, mathy day.
'''


'''
Welcome to the Calculator

What is the first number? 0
What is the second number? 1

SUM =  1.0
DIFFERENCE =  -1.0
PRODUCT =  0.0
QUOTIENT =  0.0

Have a nice, mathy day.

'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 






2. How did you decide if the functions in the `calc_util` module should return or print?





'''
