class Tv:
 def __init__(self,brand,colour):
  self.brand=brand
  self.colour=colour
 def features(self):
  print('Reliable')
class play(Tv):

 def __init__(self,model,brand,colour):
  super().__init__(brand,colour)
  self.model=model
  

 def playInfo(self):
  print("Brand:",self.brand)
  print("colour:",self.colour)
  print("model:",self.model)
d=play('LG','red', 'ax100')
d.features()
d.playInfo()
