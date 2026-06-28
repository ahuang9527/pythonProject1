class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade, **kwargs):
        super().__init__(name=name, age=age, **kwargs)
        self.grade = grade

class Teacher(Person):
    def __init__(self, name, age, dept, **kwargs):
        super().__init__(name=name, age=age, **kwargs)
        self.dept = dept

    def GetMessage(self):
        print(self.name, self.age, self.grade, self.dept)

class StuTea(Student, Teacher):
    def __init__(self, name, age, grade, dept):
        super().__init__(name=name, age=age, grade=grade, dept=dept)

test = StuTea("陈晓萌", 23, 1, "图像处理")
test.GetMessage()