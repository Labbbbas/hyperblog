import time

def fibo_gen(lim):
    # n1 = 0
    # n2 = 1
    # counter = 0

    n1, n2, counter = 0, 1, 0

    # while True:
    #     if counter == 0:
    #         counter += 1
    #         yield n1
    #     elif counter == 1:
    #         counter += 1
    #         yield n2
    #     else:
    #         aux = n1 + n2
    #         n1, n2 = n2, aux
    #         counter += 1
    #         yield aux

    while True:
        if counter < lim:
            yield n1
            n1, n2 = n2, n1 + n2
            counter += 1
        else:
            break

if __name__ == '__main__':
    # fibonacci = fibo_gen()
    for element in fibo_gen(int(input('Ingresa hasta qué número de la sucesión quieres conocer: '))):
        print(element)
        time.sleep(0.5)