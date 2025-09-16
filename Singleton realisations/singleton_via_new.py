class My_House:
  _instance = None # class variable
  
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      print("Creating Singleton instance")
      cls._instance = super().__new__(cls)
    return cls._instance


if __name__ == "__main__":
  home1 = My_House()
  home2 = My_House()
  print(type(home1))
  print(type(home2))
  print(type(My_House))
  print(home1 is home2)
