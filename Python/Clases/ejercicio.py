class Garage:
  def __init__(self, size):
    self.size = size
    self.cars = ["Ram", "Model 3"]

  def open_door(self):
    return "The door opens"
    
home = Garage(2)
print(home.cars)

# Variable = nuevos datos
home.cars = [] # en este caso ninguno

get_cars = home.cars
print(get_cars)