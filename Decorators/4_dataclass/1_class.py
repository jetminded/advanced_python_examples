class Tomato:
  def __init__(self, num, days_old, days_till_harvest):
    self.num = num
    self.days_old = days_old
    self.days_till_harvest = days_till_harvest

if __name__ == "__main__":
  garden = [Tomato(0, 10, 20), Tomato(0, 10, 20), Tomato(1, 20, 10)]

  for t in garden:
    print(t)

  print(garden[0] == garden[1])
