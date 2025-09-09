from typing import Protocol

class Eatable(Protocol):
    def eat(self):
        pass

class Apple:
    def __init__(self, color: str):
        self.color = color

    def eat(self):
        return self.color + " apple"
    
class Onion:
    def dice(self):
        print("I am crying!")

# Внизу пример Duck Typing - нам не важно, кто именно будет передан в food
# Важно, чтобы у него был метод  eat - это в Protocol
def do_eat(name: str, food: Eatable) -> None:
    print(f"{name} has eaten a " + food.eat())

if __name__ == "__main__":
    # Сработает, т.к. у Apple есть метод eat - он Eatable
    a = Apple("red")
    do_eat("Nick", a)

    # Не сработает, т.к. у Onion нет метода eat - он НЕ Eatable
    o = Onion()
    do_eat("Nick", o)
