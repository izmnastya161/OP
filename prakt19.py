#Практическая работа 19. Вариант 6
import datetime
class User:
    def __init__(self,n,s,y):
        self.name=n
        self.surname=s
        self.year=y
        self.__iq=130
    @property
    def x(self):
        return self.name,self.surname,self.year
    def get_iq(self):
        return self.__iq
class Student(User):
    def oldStudent(self):
        return int(datetime.datetime.now().strftime('%Y'))-student.year  
student=Student('Igor','Ivanov',2018)
print("Студент:",student.name,'его IQ: =',student.get_iq())

