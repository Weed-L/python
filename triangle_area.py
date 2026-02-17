height = float(input("Enter the height: "))
base = float(input("Enter the base: "))

def find_area(b, h):
    A = 0.5 * b * h
    return A
print(f"The area of the triangle is {find_area(height, base)}")
