print("Access Modifier Example:")

class A:
    public = "public variable"
    _protected = "protected variable"
    __private = "private variable"   # name mangled

class B(A):
    def show(self):
        print(self.public)
        print(self._protected)
        # print(self.__private)
        print(self._A__private)

b = B()
b.show()
