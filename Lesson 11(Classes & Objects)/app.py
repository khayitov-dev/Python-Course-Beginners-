from student import Student


student1 = Student("Jim", "Business", 3.8, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student2.gpa)
print(student1.on_honor_roll())
print(student2.on_honor_roll())