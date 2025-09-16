class Garden:
  def __init__(self, tomatoes):
    self.tomatoes_number = tomatoes

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc_value, exc_tb):
    print(f"Uprooting {self.tomatoes_number} tomatoes")

if __name__ == "__main__":
  with Garden(5) as d:
    print(f"I have {d.tomatoes_number} tomatoes!!")
  
  print("oh noooo")
