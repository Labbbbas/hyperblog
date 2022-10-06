# -*- encoding: utf-8 -*-

import random, os

def ppt(func):
    def wrapper(jugada):
        posibilidades = ['Piedra', 'Papel', 'Tijera']
        cpu = random.choice(posibilidades)
        print(f'\nLa CPU eligió: {cpu}')
        func(jugada)
        if jugada == 'Piedra' and cpu == 'Tijera'\
            or jugada == 'Papel' and cpu == 'Piedra'\
            or jugada == 'Tijera' and cpu == 'Papel':
            print('\nGanaste :D\n')
        elif jugada == cpu:
            print('\nEmpate\n')
        elif jugada == 'Tijera' and cpu == 'Piedra'\
            or jugada == 'Piedra' and cpu == 'Papel'\
            or jugada == 'Papel' and cpu == 'Tijera':
            print('\nPerdiste D:\n')
        else:
            print('\nValor inválido\n')
    return wrapper

@ppt
def tu_turno(jugada):
    print('\nElejiste: {}'.format(jugada))

if __name__ == '__main__':
    os.system('clear')
    tu_turno(str(input('\nElije piedra, papel o tijera: ')).capitalize().replace(' ',''))