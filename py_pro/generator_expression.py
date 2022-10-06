my_list = [0,1,4,7,9,10]

my_second_list = [x**2 for x in my_list]  # List Comprehension
print(my_second_list)

my_gen = (x**2 for x in my_list)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))