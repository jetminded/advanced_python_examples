def init_logger(cls):
  original_init = cls.__init__
  
  def new_init(self, *args, **kwargs):
    print(f"🆕 Creating {cls.__name__} instance")
    original_init(self, *args, **kwargs)

  cls.__init__ = new_init
  return cls
  
@init_logger
class Apple:
  def __init__(self, color):
    self.color = color

  def eat(self):
    print(f"I am eating a {self.color} apple!")


if __name__ == "__main__":
  a = Apple("red")
  a.eat()
  print()
  #print(a.__name__)
