def recursiveSum(number):
    if number <= 0:
        return 0
    else:
        i = 1
        x = 0
        for i in range(number):
            x+=i
        return number + x


if __name__ == '__main__':
    number = int(input("Type a number: "))
    print(recursiveSum(number))


# def sumaRecursiva1(num):
#     if num == 0:
#         return 0
#     return num + sumaRecursiva1(num-1)


# if __name__ == '__main__':
#     num = int(input("Type a number: "))
#     print(sumaRecursiva1(num))