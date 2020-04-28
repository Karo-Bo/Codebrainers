class Series:
    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit

    def __next__(self):
        # 1 sposób
        # temp = self.b
        # self.b = self.b + self.a
        # self.a = temp
        # 2 sposób
        self.a, self.b = self.b, self.a + self.b

        if self.a >= self.limit:
            raise StopIteration

        return self.a

    def __iter__(self):
        return Series(self.limit)
        # return self

series = Series(100)

for x in series:
    print(x)
