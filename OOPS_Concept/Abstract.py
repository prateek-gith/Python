from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(Shape):
    def __init__(self,ln,br) :
        self.lenghth=ln
        self.breadth=br
    
    def printarea(self):
        return self.lenghth*self.breadth

if __name__=='__main__':
    obj_1=rectangle(10,20)
    print(obj_1.printarea())