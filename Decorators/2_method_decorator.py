def logger(func):
  def wrapper(*args, **kwargs):
    print("Start!")
    res = func(*args, **kwargs)
    print("End!")
    return res
  return wrapper

class Apple:
  def __init__(self, color):
    self.color = color

  @logger
  def eat(self, color):
    print(f"I am eating a {color} apple")

if __name__ == "__main__":
  a = Apple("red")
  a.eat("red")
