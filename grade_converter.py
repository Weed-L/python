def main():
    print('===== Grade Converter =====')
    percent = int(input('Enter a numerical grade (1-100): '))
    grade_converter(percent)

def grade_converter(percent) :
    if percent > 100:
        print('A+')
    elif percent >= 90:
        print('A')
    elif percent >= 80:
        print('B')
    elif percent >= 70:
        print('C')
    elif percent >= 65:
        print('D')
    else:
        print('F')

main()