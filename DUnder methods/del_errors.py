class ErroredApple:
  def __del__(self):
    print("cleanup at aisle 1")
    print(1/0)

if __name__ == "__main__":
  x = ErroredApple()
  del x
  print("Hooray!")
