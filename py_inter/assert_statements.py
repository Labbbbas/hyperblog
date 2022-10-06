# -*- coding: utf-8 -*-

def divisors(num):
    list_divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            list_divisors.append(i)
    return list_divisors

def main():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa :)")
        
if __name__ == '__main__':
    main()