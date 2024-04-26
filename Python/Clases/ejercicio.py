class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
# End of starter code

class Garage:
  def __init__(self,out):
    self.out = out
    self.cars = ["Ram", "Model 3"]

  def formatter(self): 
        return f'{self.cars}'
get_cars = Garage(0)
print(get_cars.cars)