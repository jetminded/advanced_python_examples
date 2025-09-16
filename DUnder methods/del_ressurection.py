global_apple = None

class BadApple:
  def __init__(self, color):
    self.color = color

  def __del__(self):
    global global_apple
    print("Deleting a BadApple")
    global_apple = self

if __name__ == "__main__":
  x = BadApple("crimson")
  del x
  print(global_apple.color)
