class Employee:
    def __init__(self, name, position, salary):
        self.name, self.position, self.salary = name, position, salary

    def give_raise(self, amount):
        self.salary += amount
    
    def display_employee(self):
        print(f"Employee: {self.name}, Position: {self.position}, Salary: ${self.salary}")

employee1 = Employee("Gibea", "Education", 50000)
employee1.give_raise(5000)
employee1.display_employee()