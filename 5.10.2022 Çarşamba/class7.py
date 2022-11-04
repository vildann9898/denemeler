class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self): # örneğe ait grade'i döndürüyor
        return self.grade

class Course():
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students: 
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        a = 0
        for i in self.students: # i döngülerde sırayla s1 ve s3 oluyor
            a += i.get_grade() # a += s1.get_grade(), a += s3.get_grade()
        return a / len(self.students) #ortalamayı yolluyor
        
s1 = Student("Musa",23,90) #Student classından nesneler oluşturuyoruz (örnekleme)
s2 = Student("Mehmet",19,70)
s3 = Student("Ayşe",24,0)
c1 = Course("Python",2) #Course classından nesneler oluşturuyoruz
c2 = Course("C#",3)
c1.add_student(s1) # c1 Course nesnesine s1 öğrencisini ekliyoruz
c1.add_student(s3)
print(c1.get_average_grade()) #c1 course nesnesinin methodunu çağırıyoruz.
c1.add_student(s2) 
print(c1.get_average_grade())