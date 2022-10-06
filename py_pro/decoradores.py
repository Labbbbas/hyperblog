def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

@decorador
def saludo():
    print('Hola')

# def run(saludo):
#     saludo = decorador(saludo)
#     saludo()

def run():
    saludo()
    
if __name__ == '__main__':
    run()