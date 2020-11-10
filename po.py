#is a inheritance
class Person:
 def __init__(self,name,age):
  self.name=name
  self.age=age
 def eatndrink(self):
  print('Eat and Drink')
class Developer(Person):
 def __init__(self,name,age,eno,esal):
  super().__init__(name,age)
  self.eno=eno
  self.esal=esal
 def code(self):
  print("Busy with Coding in Python")

 def developerInfo(self):
  print("Name:",self.name)
  print("Age:",self.age)
  print("Number:",self.eno)
  print("Salary:",self.esal)
d=Developer('Ram', 48, 100, 10000)
d.eatndrink()
d.code()
d.developerInfo()
