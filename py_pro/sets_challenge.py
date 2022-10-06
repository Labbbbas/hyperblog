import os

montapuercos = {'Velocidad: Muy Alta', 'Tipo: Tropa', 'Objetivos: Estructuras', 'Calidad: Especial', 'Coste de Elixir: 4'}
minipekka = {'Velocidad: Alta', 'Tipo: Tropa', 'Objetivos: Terrestres', 'Calidad: Especial', 'Coste de Elixir: 4'}

union = montapuercos | minipekka

interseccion = montapuercos & minipekka

diferencia1 = montapuercos - minipekka
diferencia2 = minipekka - montapuercos

diferencia_simetrica = montapuercos ^ minipekka

if __name__ == '__main__':
    os.system('clear')  # Linux y Mac
    # os.system('cls')  # Windows
    print(f'\nUnión: {union}\n')
    print(f'Similitud: {interseccion}\n')
    print(f'Diferencia montacerdos - aña: {diferencia1}\n')
    print(f'Diferencia aña - montacerdos: {diferencia2}\n')
    print(f'Diferencia simétrica: {diferencia_simetrica}\n')