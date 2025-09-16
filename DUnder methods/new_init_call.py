class Apple:

  def __new__(cls):
    print("__new__ method called")
    # creates an instance of a class
    # but who is super???
    return super().__new__(cls)

  def __init__(self):
    # initializes fields of a class
    print("__init__ method called")

  def __call__(self):
    print("__call__ method called")

if __name__ == "__main__":
  a = Apple()
  # hint for a question above
  print("Type of an int: ", type(int))
  print("Type of an apple: ", type(Apple))
  print("Type of apple instance a: ", type(a))
