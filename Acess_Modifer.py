class Dada:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def getName(self):
        return self.name


class Mama:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def getName(self):
        return self.name


class Son:
    def __init__(self, name=None, age=None, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother

    def __str__(self):
        return f"My Name is {self.name} and my age is {self.age}"

    def parentsNames(self):
        return f"My Father Name is {self.father.getName()} and My Mother Name is {self.mother.getName()}"


dada = Dada("Mariappan", 51)
mama = Mama("Radha", 56)
MySon = Son("Kishore Ram M", 20, dada, mama)

print(MySon.parentsNames())
