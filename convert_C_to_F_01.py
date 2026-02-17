celsius = float(input("Enter a temperature in Celsius: "))

def convert_c_to_f(c):
    F = c * (9/5) + 32
    return F
print(f"{celsius} degrees Celsius is {convert_c_to_f(celsius)} degrees Fahrenheit.")
