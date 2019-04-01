# #практическая работа 18
# #наследование и перегрузка
# #вариант 6
# #класс студент который будет наследоваться 
# # от класса юзер(свойства name,year,surname)(метод-который
# # рассчитывает на каком курсе учится студент(год узнать)).Студент должен 
import datetime
class User:
    def __init__(self,n,s,y):
        self.name=n
        self.surname=s
        self.year=y
    @property
    def x(self):
        return self.name,self.surname,self.year
class Student(User):
    def oldStudent(self):
        return int(datetime.datetime.now().strftime('%Y'))-student.year
student=Student('Igor','Ivanov',2018)
print(student.name,student.surname,student.year)
print('Курс:',student.oldStudent())