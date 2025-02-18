class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am studying {self.course}.")

student1 = Student("GIBEA", 21, "IT")
student2 = Student("RAMIL", 20, "IT")
student3 = Student("JUNKO",22, "IT")

student1.introduce()
student2.introduce()
student3.introduce()
