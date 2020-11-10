class Car:
 def __init__(self,brand,colour):
  self.brand=brand
  self.colour=colour
 def autoPilot(self):
  print('moving')
class move(Car):

 def __init__(self,model,brand,colour):
  super().__init__(brand,colour)
  self.model=model
  
 def autogear(self):
  print("Exit")

 def moveInfo(self):
  print("Brand:",self.brand)
  print("colour:",self.colour)
  print("model:",self.model)
d=move('BMW','red', 'ax100')
d.autoPilot()
d.autogear()
d.moveInfo()
