# Sin sets
# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

# def run():
#     my_list = [1, 1, 2, 2, 4]
#     print(remove_duplicates(my_list))


# Con sets
def remove_duplicates(some_list):
    return list(set(some_list))

def run():
    my_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(my_list))

    
if __name__ == '__main__':
    run()