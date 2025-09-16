from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def eat(self):
        pass
    
    # Тут также могут быть какие-то другие методы, общие для всех классов

class Apple(Fruit):
    def eat(self):
        print("I have eaten an apple!")

class Onion(Fruit):
    def dice(self):
        print("I am crying!")
 
if __name__ == "__main__":
    # Сработает, всё ок
    a = Apple()
    a.eat()


    print(type(a))
    print(type(Apple))
    print(type(Fruit))

    # Не сработает, т.к. в классе Onion не определен метод eat у класса Onion
    # А должен быть, т.к. мы унаследовали его от Fruit
    o = Onion()
    o.dice()
