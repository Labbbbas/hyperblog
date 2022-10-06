from math import sqrt

def main():
    dict_sqrt = {i:round(sqrt(i),3) for i in range(1, 101)}

    print(dict_sqrt)

if __name__ == '__main__':
    main()