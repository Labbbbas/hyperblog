# -*- coding: utf-8 -*-

from lamp import Lamp
import os 

def run():
    lamp = Lamp(is_turned_on=False)


    while True:
        command = str(input('''
            ¿Qué desea hacer?

            [p] Prender la lámpara
            [a] Apagar la lámpara
            [s] Salir
        '''))

        os.system('clear')
        
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()