class person:
   def ___init__(self, name, s_name):
     self.name = name
     self.s_name = s_name

     def printname(self):
      print(self.name, self.s_name)

class Student(person):
   pass
x = Student('hassan', 'mohamed')
x.printname()