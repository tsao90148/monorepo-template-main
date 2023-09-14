from abc import ABC, abstractclassmethod

"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
class Shape(ABC):
    """abstract class shape has set_value and area functions"""
    @abstractclassmethod
    def set_value(self,width,height):
        pass

    @abstractclassmethod
    def area(self):
        pass

class Rectangle(Shape):
    """class rectangle is a subclass of abstract class shape"""
    def set_values(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle()

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
