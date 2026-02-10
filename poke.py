from stats import pikachu


print('Hello!  - ')
print('Pikachu', 'Eeve', 'Lukario')
first_pokemon = int(input('Choose your first Pokemon(1,2,3) - '))
if first_pokemon == 1:
    print('Great choice!')
    print('Do you want to see the statistics? ')
    stats = input('Stats(1-yes): ')
    if stats == '1':
        print(pikachu)
        name = input('What do you want to name it? - ')
        print(f'Great choice - {name}')
        print('Now what?')
    else:
        print('go away')


