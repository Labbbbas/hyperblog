def my_gen():
    
    print('Hola')
    n = 0
    yield n 

    print('Estoy utilizando')
    n = 1
    yield n

    print('Generadores')
    n = 2
    yield n

a = my_gen()

print(next(a))  # Hola
print(next(a))  # Estoy utilizando
print(next(a))  # Generadores
print(next(a))  # StopIteration