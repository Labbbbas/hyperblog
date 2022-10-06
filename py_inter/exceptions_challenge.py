# -*- coding: utf-8 -*-

def divisors(num):
    divisors = [i for i in range(1, num+1) if num%i==0]
    
    return divisors
    
def main():
    try:
        num = int(input("Ingresa un número: "))
        if num <= 0:
            raise ValueError
        print(divisors(num))
        print("Terminó mi programa :)")
    except ValueError:
        print("No puedes ingresar números negativos o neutros :(")
        
if __name__ == '__main__':
    main()