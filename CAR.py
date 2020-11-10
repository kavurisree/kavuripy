class Car:
 def __init__(self,brand,colour):
  self.brand=brand
  self.colour=colour
 def start(self):
  print('start the car')
class move(Car):

 def __init__(self,model,brand,colour):
  super().__init__(brand,colour)
  self.model=model
  
 def stop(self):
  print("Exit through door")

 def moveInfo(self):
  print("Brand:",self.brand)
  print("colour:",self.colour)
  print("model:",self.model)
d=move('Waganor','red', 'ax100')
d.start()
d.stop()
d.moveInfo()
