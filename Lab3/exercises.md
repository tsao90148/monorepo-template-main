# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	-  Abstract class typically cannot be instantiated and usually says @abstractmethod above its methods. In the code, there's also no abc module used. MObject should be a concrete class since it has __init__ function inside.
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- __del__ method is a finalizer that is sometimes called a destructor. It basically is called when an object is collected as garbage after all the object's reference is deleted.
1. What class does Texture inherit from?
	- According to the "class Texture(Image):" line in the code, texture inherits from the Image class and all its methods.  
1. What methods and attributes does the Texture class inherit from 'Image'? 
	- All methods including getWidth, getHeight, getPixelColorR, getPixel, and setPixelsToRandomValue methods and m_width, m_height, m_colorChannels, and m_pixels attributes are inherited from the Image class.  
1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- The relationship between texture and image should be a "is-a" relationship. This is because texture is not a composition and when texture is removed, it will not affect the image class itself. However, this does not work the other way around.  
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes, python has a default constructor when none is defined. 

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
In a single thread, yes but not in a multi-thread environment. In multi-thread, instances are created simultaneously in different threads.   
