my_set1 = {3,4,5}
my_set2 = {5,6,7}

union = my_set1 | my_set2
print(union)

interseccion = my_set1 & my_set2
print(interseccion)

diferencia = my_set1 - my_set2
print(diferencia)
diferencia2 = my_set2 - my_set1
print(diferencia2)

diferencia_simetrica = my_set1 ^ my_set2
print(diferencia_simetrica)