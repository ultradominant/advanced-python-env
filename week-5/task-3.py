class Person:
    def __init__(self, name):
        self._name = name 

    def introduce(self):
        return f"My name is {self._name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self):
        return f"I am student {self._name}, ID: {self.student_id}"

person = Person("John")
student = Student("Alice", "S123")

print(person.introduce())
print(student.introduce())
