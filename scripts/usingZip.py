from time import sleep

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spider Man', 'Superman', 'Deadpool', 'Batman']

identities = list(zip(names, heroes))

print('''ZIP uni valores de diferentes listas em tuplas,
então o que antes era isso: ''')
print(names)
print(heroes)

sleep(4)
print('Se torna isso: ')
print(identities)
sleep(4)

for identity in identities:
    print(f'{identity[1]} is {identity[0]}!')
