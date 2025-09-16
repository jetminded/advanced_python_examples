def singleton(cls):
  instances = {}

  def get_instance(*args, **kwargs):
    if cls not in instances:
      instances[cls] = cls(*args, **kwargs)
    return instances[cls]

  return get_instance


@singleton
class House:
  def __init__(self, owner):
    self.owner = owner

#class MyHouse(House):
#  def __init__(self, owner, color):
#    super().__init__(owner)
#    self.color = color

if __name__ == "__main__":
  home1 = House("Nick")
  home2 = House("Not Nick")
  print(type(home1))
  print(home1.owner)
  print(type(home2))
  print(home2.owner)
  print()
  print(type(House))
  print()
  print(home1 is home2)

  #print(" ================ ")
  #home3 = MyHouse("Nick", "blue")
  #home4 = MyHouse("Not Nick", "red")
  #print(home3.owner)
  #print(home3.color)
  #print(home4.owner)
  #print(home4.color)
