class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

class House(metaclass=Singleton):
  def __init__(self, owner):
    self.owner = "Nick"

class MyHouse(House):
  def __init__(self, owner, color):
    super().__init__(owner)
    self.color = color

if __name__ == "__main__":
  print(type(House))
  h1 = House("Nick")
  h2 = House("Not Nick")
  print(h2.owner)

  #print("====")
  #mh = MyHouse("Not Nick", "red")
  #print(mh.owner)
  #print(mh.color)
