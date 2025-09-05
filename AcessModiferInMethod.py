class M:
    def public(self):
        print("Public Method")

    def _protected(self):
        print("Protected Method")

    def __private(self):
        print("Private Method")


class A(M):  # Inheriting from M
    def show(self):
        self.public()
        self._protected()
        # self.__private()
        self._M__private()



# create object
c = A()
c.show()
