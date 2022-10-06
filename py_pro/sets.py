def ejemplo1():
    my_set = {3,4,5}
    my_set2 = {'Hola', 23.3, False, True}
    my_set3 = {3,3,2}
    # my_set4 = {[1,2,3], 4}  # No puedes meter listas a sets\

    print('my_set =', my_set)
    print('my_set2 =', my_set2)
    print('my_set3 =', my_set3)
    # print('my_set4 =', my_set4)


def ejemplo2():
    empty = {}
    print(type(empty))  # Python entiende que es un diccionario

    empty_set = set()
    print(type(empty_set))  # Ahora sí es un set


def ejemplo3():
    #  set no ayuda a eliminar los repetidos para siempre
    my_list = [1,1,2,2,3,3,4,4,5,5]
    my_set = set(my_list)
    print(my_set)
    x = list(my_set)
    print(x)

    my_tuple = ('Hola', 'Hola', 'Hola', 4)
    my_set2 = set(my_tuple)
    print(my_set2)


def ejemplo4():
    my_set = {1,2,3}
    print(my_set)

    # Añadir sólo un elemento
    my_set.add(4)
    print(my_set)

    # Añadir múltiples elementos
    my_set.update([1,2,5])  # Saca los elementos y agrega los no repetidos
    print(my_set)

    my_set.update((1,7,2), {6,8})
    print(my_set)


def ejemplo5():
    my_set = {1,2,3,4,5,6,7}
    print(my_set)

    my_set.discard(1)  # Elimina un elemento existente
    print(my_set)

    my_set.remove(2)  # También elimina un elemento existente
    print(my_set)

    my_set.discard(10)  # Intenta eliminar un elemento inexistente
    print(my_set)

    my_set.remove(12)  # Intenta eliminar un elemento inexistente pero da error
    print(my_set)


def ejemplo6():
    my_set = {0,1,2,3,4,5,6,7}
    print(my_set)

    my_set.pop()  # Borra el primer elemento de la lista  
    print(my_set)

    my_set.clear()  # Borra todo el set
    print(my_set)


if __name__ == '__main__':
    # ejemplo1()
    # ejemplo2()
    # ejemplo3()
    # ejemplo4()
    # ejemplo5()
    ejemplo6()