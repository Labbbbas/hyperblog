from datetime import date, datetime

def execution_time(func):
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron {} segundos'.format(time_elapsed.total_seconds()))
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 10000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre='César'):
    print(f'Hola {nombre}')

saludo('Fernando')
suma(5, 5)
random_func()