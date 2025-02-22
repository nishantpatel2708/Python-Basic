class A:
    a = 10      ##Public
    _b = 20     ##Protected
    __c = None  ##Private

    print(a, _b, __c)
    
    def Add(self):
        self.__c = self.a + self._b
        print(self.__c)


class B(A):
    def Show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

obj = B()
obj.Show()

# print(obj.a)
# print(obj._b)
# print(obj.__c)
