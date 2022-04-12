from functools import wraps


class WowClass:
    def init(self, inlist):
        self.inlist = inlist

    def iter(self):
        self.i = 0
        return self

    def next(self):
        if self.i >= len(self.inlist):
            raise StopIteration
        result = self.inlist[self.i]
        self.i += 1
        return result

    def call(self, function):
        def wrapper():
            print(next(self.my_generator()))

        return wrapper

    def my_generator(self):
        if self.i >= len(self.inlist):
            self.i = 0
        result = self.inlist[self.i]
        self.i += 1
        yield result

    def add(self, other):
        for item in other.inlist:
            self.inlist.append(item)
        print(self.inlist)


def main():
    a = WowClass([1, 2, 3, 4, 5, 99])

    @a
    def my_func():
        return 5

    # for i in range(15):
    #     my_func()

    # for i in a:
    #     print(i)
    #
    # for i in a:
    #     print(i)

    a += WowClass([6, 7])


if __name__ == '__main__':
    main()