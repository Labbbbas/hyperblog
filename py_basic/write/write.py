def run():
    with open('./numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))
            f.write('\n')

    # try:
    #     f = open()
    # finally:
    #     f.close()


if __name__ == '__main__':
    run()