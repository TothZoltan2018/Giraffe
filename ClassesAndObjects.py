class Student:
   def __init__(self, name, major, gpa, is_on_probation):
       self.name = name
       self.major = major
       self.gpa = gpa
       self.is_on_probation = is_on_probation
   def on_honor_roll(self):
       if self.gpa >= 3.5:
           return True
       else:
           return False

# from ClassesAndObjects import Student  # itt nem kell, mert egy fajlban vagyunk az osztalydefinicioval
Student1 = Student("Jim", "Business", 3.1, False)

print(Student1.name)


# ############################ Classs Functions ############################
student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyillis", "Business", 3.8, False)

print(student1.on_honor_roll())