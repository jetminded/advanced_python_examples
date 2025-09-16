class DeletedApple:
  def __del__(self):
    print(f"{self.__class__.__name__}.__del__")

  def __delitem__(self, key):
    print(f"{self.__class__.__name__}.__delitem__")

  def __delattr__(self, item):
    print(f"{self.__class__.__name__}.__delattr__")

if __name__ == "__main__":
  x = DeletedApple()
  del x[0]
  del x.color
  print("start")
  del x # Does it call __del__?
  print("end")

  x = DeletedApple()
  y = x
  print(y is x)
  print("start2")
  del x 
  print("end2")
  # RefCount = 0?
