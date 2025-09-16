class CircledApple:
  def __del__(self):
    print("Cleanup please")

if __name__ == "__main__":
  x = CircledApple()
  y = CircledApple()
  print(x is y)
  x.child = [y]
  y.parent = x

