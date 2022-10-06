import os

def is_prime(number: int) -> bool:

    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            print(i)
            if number % i == 0:
                return False

    return True
        
        
def run():
    os.system('clear')
    number = int(input('What number do you want to know if is it prime? '))

    if is_prime(number):
        print('{} is a prime number'.format(number))
    else:
        print('{} is not a prime number'.format(number))


if __name__ == '__main__':
    run()