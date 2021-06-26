class MyClass(object):
    __slots__ = ['name', 'id']

    def __init__(self, name, id):
        print(locals())
        self.name = name
        self.id = id

    def __iter__(self):
        return iter([self.name, self.id])

    def __reversed__(self):
        return [self.id, self.name]

    def __str__(self):
        return self.name + ' ' + str(self.id)

    def __len__(self):
        return 2

    def __enter__(self):
        print("entered class")

    def __exit__(self, t, v, tb):
        print("exited: " + str(t) + " " + str(v))


with MyClass('abc', 101) as f:
    pass

