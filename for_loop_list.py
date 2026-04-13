def main():
    doggo_names = get_doggo_names()
    output_names(doggo_names)

def get_doggo_names():
    name = ''
    names = []
    while name != 'DONE':
        name = input('Name of doggo: ')
        if name != 'DONE':
            names.append(name)

    return names

def output_names(doggo_names):
    for name in doggo_names:
        print(f"Name of Doggo: {name}")
    print()
    for name in doggo_names:
        print(f"{name} is awesome.")


main()