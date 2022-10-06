def simple():
    my_list = [1,2,3,4,5]
    my_iter = iter(my_list)

    # print(next(my_iter))  # 1
    # print(next(my_iter))  # 2
    # print(next(my_iter))  # 3
    # print(next(my_iter))  # 4
    # print(next(my_iter))  # 5
    # print(next(my_iter))  # StopIteration error

    while True:
        try:
            element = next(my_iter)
            print(element)
        except StopIteration:
            break


class EvenNumbers():
        def __init__(self, max=None):
            self.max = max

        def __iter__(self):
            self.num = 0
            return self

        def __next__(self):
            if not self.max or self.num <= self.max:
                result = self.num
                self.num += 2
                return result
            else:
                raise StopIteration


if __name__ == '__main__':
    # simple()

    for element in EvenNumbers(int(input('Indique hasta el número que quiere parar: '))):
        print(element)