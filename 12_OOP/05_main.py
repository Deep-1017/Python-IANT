class Student:
    school_name = "Hogwarts Academy"  # Class variable 
    total_students = 0   
    
    def __init__(self, name, marks):
        self.name = name    # Instance variable
        self.marks = marks  # Instance variable
        Student.total_students += 1

s1 = Student("Ravi", 85)
s2 = Student("Priya", 92)   


# s1.marks = 90

print(Student.school_name)    # Hogwarts Academy
print(s1.school_name)         # Hogwarts Academy (accessible via instance too)
print(Student.total_students)

Student.school_name = "IANT Institute"
print(s1.school_name)  # Durmstrang Institute
print(s2.school_name)  # Durmstrang Institute