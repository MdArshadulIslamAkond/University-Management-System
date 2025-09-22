class Person:
    
    total_people = 0
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.total_people +=1
    
    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."
        
    @classmethod
    def get_total_people(cls):
        return f"Total people created: {cls.total_people}"
    
    
class Student(Person):
    
    def __init__(self, name: str, age: int, student_id: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list: list[str] = []
        self.__gpa = 0.0 # private attribute
        
        
    def enroll_course(self, course: str):
        self.course_list.append(course)

    def show_courses(self):
        return f"Enrolled courses: {', '.join(self.course_list)}"

    # GPA property with encapsulation
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value: float):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    @staticmethod
    def is_valid_id(student_id: str):
        return student_id.startswith("S-")


class Teacher(Person):
    def __init__(self, name: str, age: int, employee_id: int, subject: str):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject =  subject
        
        
      # Method overriding
    def introduce(self):
        return f"I am Professor {self.name}, teaching {self.subject}."
    
class GraduateStudent(Student):
    def __init__(self, name: str, age: int, student_id: str, thesis_title: str):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title   
    
# --- Polymorphism ---
def display_role(person: Person):
    if isinstance(person, Student):
        return f"{person.name} is a Student."
    elif isinstance(person, Teacher):
        return f"{person.name} is a Teacher."
    else:
        return f"{person.name} is a Person."
    
    
    
    
# ----- Demo------------

# Create objects
p1 = Person("Alice", 40)
s1 = Student("Bob", 20, "S-101")
t1 = Teacher("Dr. Smith", 50, "T-200", "Physics")
g1 = GraduateStudent("Charlie", 25, "S-202", "AI in Healthcare")

# Use methods
print(p1.introduce())
print(s1.introduce())
print(t1.introduce())
print(g1.introduce())

# Student enrolls courses
s1.enroll_course("Math")
s1.enroll_course("Programming")
print(s1.show_courses())

# GPA encapsulation
s1.gpa = 3.8
print("Bob's GPA:", s1.gpa)

# Static method
print("Valid ID?", Student.is_valid_id("S-101"))

# Polymorphism
print(display_role(s1))
print(display_role(t1))

# Class method
print(Person.get_total_people())