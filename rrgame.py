'''
from random import randint
num = None

print('Угадай Число')

chislo = randint(1, 100)
while num != chislo:
    num = int(input(' от 1-100  - '))

    if num > chislo:
        print('Cлишком большое')
    elif num < chislo:
        print('Слишком мало')
    else:
        print(f'Correct! The number is - {chislo}')
'''

from random import randint
print('Угадай число')
num = None
chislo = randint(1, 100)
while (num := int(input('от 1-100 - '))) != chislo:
    print('Слишком большое' if num > chislo else 'Слишком мало')
print(f'Correct! The number is - {chislo}')

