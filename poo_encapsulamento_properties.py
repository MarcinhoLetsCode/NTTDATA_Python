#Properties()

class Foo:
    def __init__(self, y=None):
        self._x = y

    @property
    def y(self):
        return self._x or 0

    @y.setter
    def y(self, value):
        _x = self._x or 0
        _value = value or 0
        #self._x = _x + _value
        self._x += _value

    @y.deleter
    def y(self):
        self._x = -1
        #del self._x
    
foo = Foo(10)
print(foo.y)
foo.y = 10
print(foo.y)
del foo.y
print(foo.y)
