# 🔹 1. Instance Methods

* Defined with `def method(self, ...)`
* The **most common type of method**.
* They operate on **instance variables** (data specific to each object).
* `self` represents the object (instance) itself.

✅ Example:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name       # instance variable
        self.marks = marks
    
    def show(self):  # instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Kishore", 85)
s2 = Student("Radha", 92)

s1.show()   # uses s1’s data
s2.show()   # uses s2’s data
```

📌 **Key:**

* Works with instance data (`self.name`, `self.marks`)
* Different objects have different values.

---

# 🔹 2. Class Methods

* Defined with `@classmethod` decorator.
* First argument is `cls` (class itself).
* Used to access or modify **class variables** (shared across all objects).

✅ Example:

```python
class Student:
    school_name = "ABC School"   # class variable
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_school(cls, new_name):  # class method
        cls.school_name = new_name     # modify class variable

s1 = Student("Kishore")
s2 = Student("Radha")

print(Student.school_name)  # ABC School
Student.change_school("XYZ School")
print(Student.school_name)  # XYZ School
```

📌 **Key:**

* Class methods are useful when you want to **affect all objects at once**.
* Commonly used for **factory methods** (creating objects in different ways).

---

# 🔹 3. Static Methods

* Defined with `@staticmethod` decorator.
* Do **not take `self` or `cls`** as the first argument.
* Behaves like a **normal function inside a class**, but kept there for **logical grouping**.

✅ Example:

```python
class MathUtils:
    @staticmethod
    def add(x, y):   # no self, no cls
        return x + y

print(MathUtils.add(10, 20))   # 30
```

📌 **Key:**

* No access to instance (`self`) or class (`cls`) data.
* Just a helper function inside a class.
* Used for **utility functions** related to the class.

---

# 🔎 Difference Summary

| Type         | Decorator       | First Arg | Can Access Instance Vars? | Can Access Class Vars? | Typical Use Case                         |
| ------------ | --------------- | --------- | ------------------------- | ---------------------- | ---------------------------------------- |
| **Instance** | none            | `self`    | ✅ Yes                     | ✅ Yes                  | Work with object’s data                  |
| **Class**    | `@classmethod`  | `cls`     | ❌ No                      | ✅ Yes                  | Modify class-level data, factory methods |
| **Static**   | `@staticmethod` | none      | ❌ No                      | ❌ No                   | Utility/helper functions                 |

---

# 🎯 Real-World Example (All 3 together)

```python
class Employee:
    company = "Google"   # class variable
    
    def __init__(self, name, salary):
        self.name = name       # instance variable
        self.salary = salary

    # instance method
    def show(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    # class method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # static method
    @staticmethod
    def is_high_salary(salary):
        return salary > 50000


# Usage
e1 = Employee("Kishore", 40000)
e2 = Employee("Radha", 60000)

e1.show()   # Employee: Kishore, Salary: 40000, Company: Google
e2.show()   # Employee: Radha, Salary: 60000, Company: Google

Employee.change_company("Microsoft")  # affects all employees

e1.show()   # Company changed to Microsoft
e2.show()

print(Employee.is_high_salary(40000))   # False
print(Employee.is_high_salary(60000))   # True
```

---

✅ So in short:

* **Instance methods** → deal with object’s own data.
* **Class methods** → deal with data common to all objects.
* **Static methods** → helper functions, logically inside the class, but independent.
