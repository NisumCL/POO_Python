from abc import abstractmethod, ABCMeta

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def caminar(self):
        pass

    def comer(self):
        print("Animal comerá")

animal = Animal()

