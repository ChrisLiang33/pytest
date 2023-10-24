class Classroom:
    def __init__(self, teacher, student, course_title):
        self.teacher = teacher
        self.student = student
        self.course_title = course_title
    def add_student(self, student):
      if len(self.student) <= 10:
         self.student.append(student)
      else:
         raise TooManyStudents
    
        