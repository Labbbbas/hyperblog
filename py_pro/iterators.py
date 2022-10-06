import os, time

class FiboIter():
    def __init__(self, limit: int):
        self.limit = limit

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if self.counter <= self.limit:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration

if __name__ == '__main__':
    os.system('clear')  # Linux y Mac
    # os.system('cls')    # Windows
    fibonacci = FiboIter
    for element in fibonacci(int(input('Indique hasta qué número de la secuencia desea conocer: '))-1):
        print(element)
        time.sleep(0.5)