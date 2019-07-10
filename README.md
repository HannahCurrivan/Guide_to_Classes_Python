# A guide to making classes in python:

## What is a class:
Classes are with the area of Oject Oriented Programming. What is Oject Oriented Programming? This offers programmers a means of structuring programs so that properties and behavours are but together into a single **object**.

## How to use class:
Let's start with making a class called **rocket** and within this class we set a "What type of rocket it is?", which we use in this example we are saying that we are "Space Rockets". 

```python
class rocket:

    types = "Space Rockets"
    
```
## Using functions within the class:

Then within this call we can use a function, and this function will have *_Init_* which is known as a constructor in object oriented concepts, this method  called when an object is created from the class and it allow the class to initialize the attributes of a class. 
Example: Let's consider the "name" and the "year" which these rockets where launched.
The function will have a *self* which represents the instance of the class, this word will give use access the attributes and methods of the class. 
Here is the example function:

```python
class rocket:

    types = "Space Rockets"
    
    
    def _init_(self, name, year):
        self.name = name
        self.year = year
        
```

## Using the ojects:

Now we can use these objects:
```python 
rocket1 = rocket("Saturn 5", 1967)
rocket2 = rocket("Ariane 5", 1996) 

print("{} first launch was in {}, and {} first launch was in {}".format(rocket1.name, rocket1.year, rocket2.name, rocket2.year))
```

## Using the ojects within a if statement: 

We can even put the class through a *if* statement:

```python 
if rocket1.types == "Space Rockers":
    print("{0} was first launched in {1}!".format(rocket1.name, rocket1.year))
```


