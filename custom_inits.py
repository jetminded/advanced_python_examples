class Datetime:
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    @classmethod
    def today(cls):
        y, m, d = list(map(int, tdy.split()))
        return cls(y, m, d)
 
tdy = "2025 09 09"


if __name__ == "__main__":
    # old
    y, m, d = list(map(int, tdy.split()))
    now = Datetime(y, m, d)
    # new
    now = Datetime.today()
