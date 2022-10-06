def main():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"first_name":"Fernando", "last_name":"Labastida"}

    super_list = [
        {"first_name":"Fernando", "last_name":"Labastida"},
        {"first_name":"Miguel", "last_name":"Torres"},
        {"first_name":"Pepe", "last_name":"Bautista"},
        {"first_name":"Diego", "last_name":"Vazquez"},
        {"first_name":"Quetzalli", "last_name":"Lopez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')


if __name__ == '__main__':
    main()