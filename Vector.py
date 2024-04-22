class Vector:
    def __init__(self, content):
        self.content = content
        self.len = len(content)

    def __add__(self, other):
        lis = []
        for index in range(self.len):
            lis.append(self.content[index] + other.content[index])
        return Vector(tuple(lis))

    def __sub__(self, other):
        lis = []
        for index in range(self.len):
            lis.append(self.content[index] - other.content[index])
        return Vector(tuple(lis))

    def __mul__(self, other):
        lis = []
        for index in range(self.len):
            lis.append(self.content[index] * other)
        return Vector(tuple(lis))

    def __truediv__(self, other):
        lis = []
        for index in range(self.len):
            lis.append(self.content[index] / other)
        return Vector(tuple(lis))

    def __str__(self):
        return str(self.content)

    def __getitem__(self, item):
        return self.content[item]

    def __setitem__(self, key, value):
        lis = list(self.content)
        lis[key] = value
        self.content = tuple(lis)