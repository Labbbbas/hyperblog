def main(n):
    def repetidor(palabra):
        assert type(palabra) == str, 'Sólo puedes ingresar strings'
        return palabra * n
    return repetidor

def run():
    palabra_input = main(int(input('Ingrese cuántas veces quiere repetir una palabra: ')))
    print(palabra_input(input('Ingrese la palabra: ')))

if __name__ == '__main__':
    run()