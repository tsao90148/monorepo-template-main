# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matters. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes, functions such as append, extend, insert, and remove are all pretty accurate in describing their actual function/what it does. Most of the functions in the list and dictionary have accurate verb names. Only a few are not such as pop. 

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

lists are considered as sequence types like tuples and ranges. Dictionaries are mapping data types. Lists are also ordered while dictionaries are not. You can access the list by its index while for dictionaries, you will need the key.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes, as long as you know the index of the element, you can access it in the list. This allowing for random access is one of the list's key characteristics. 

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

pros: these container structures are very flexible and can store any data type since they can work with any data type. However, this also makes it less predictable since it can contain different data types.  
## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

I think they are well-named. Head sends a head request, get sends a get request and post sends a post request. 
Function name generally tells you what type of request is being sent. 

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, functions such as resolve_redirects have more than 5 arguments. There are also other functions that has a lot of arguments. However, most of these arguments are defaulted to none. So it is possible to not need more than 5 arguments to use these functions.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

**kwargs is a special argument that gives users flexibility. It can be used to accept additional named arguments even if the function's parameter list is not changed. However, this flexibility also means that it is more unclear for the users and this may also have name conflicts when used often.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


Some arguments cannot be set to none since it may be necessary for the function to run. If the argument is optional, it can be set to none to make it easier for users to use. It is also possible to set arguments to a specific default value. This makes sure that only users know what they are trying to do to change the value of the argument. 