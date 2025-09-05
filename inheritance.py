class A:
    def printA(self):
         return  print("A")
class B(A):
    def printB(self):
         return  print("B")
b =B()
b.printA()