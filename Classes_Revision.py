# PYTHON CLASSES AND OBJECTS: FOUNDATIONAL GUIDE

# CONCEPT 1: WHAT IS CLASS?
# A class is a "blueprint" or "template"
# It defines the structure (data/attributes) and behaviors (functions/methods)
# that something will have. However, the class itself is not the actual "thing".
# Think of a class as the architectural drawing of a house, not the house itself.


class Dog:
    # The 'pass' keyword is used to create an empty block of code.
    # For now, this is just an empty blueprint with no rules yet.
    pass


# CONCEPT 2: CREATING AN OBJECT (INSTANTIATION)
# An object is a specific, tangible instance created from  a class blueprint.
# If 'Dog' is the blueprint, the object is the actual, living dog.
# Creating an object is called "instantiating" a class

# We create an object by calling the class name followed by parentheses ()
my_dog = Dog()


# Concept 3: THE __init__ METHOD AND 'self'
# __init__ is a special method (called a "constructor")
# It runs AUTOMATICALLY the exact moment a new object is created.
# Its job is to set up the initial state (attributes) of that specific object

# 'self' is a refrence to the specific object being created.
# It allows  the object to store data unique to itself.
# You NEVER pass 'self' manually when calling a method; Python does it
# automatically behind the scenes.


class Person:
    # The contructor requires 'name' and 'age' when we create the object
    def __init__(self, name, age):
        # 'self.name' binds the provided name to THIS specific object instance
        self.name = name
        # 'self.age' binds the provided age to THIS specific object instance
        self.age = age

    # A "method" is simple a function defined inside a class
    # It defines behavior. It must take 'self' as the first parameter
    # So it can access the object's own data
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Let's create two distinct objects (instances) from the Person blueprint
# Notice how we only pass 'name' and 'age'. Python handles 'self' automatically.
person1 = Person("Alice", 30)
person2  = Person("Bob", 25)

# We call the method on the specific objects.
# Each object remembers its own unique data.
person1.introduce() # # Hello, my name is Alice and I am 30 years old.
person2.introduce()



# Concept 4: PASSING AN OBJECT TO ANOTHER CLASS (COMPOSITION)
# Classes can iteract. One class can hold an object of another class as one
# of its attributes. This is called "composition" (a "has-a" relationship).
# Example: A Car HAS AN Engine. The Car class will accept an Engine object.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine starting with {self.horsepower} horsepower. Vroom!")


class Car:
    def __init__(self, model, engine_object):
        self.model = model

        # CRITICAL: We are storing an entire Engine OBJECT inside the Car object.
        # "engine_object" is the variable name we used in the parameters.
        # 'self.engine' is the attribute name this specific Car will use to remember it.
        self.engine = engine_object

    def drive(self):
        print(f"The {self.model} is ready to drive.")

        # Because 'self.engine' holds an Engine object, we can call its methods!
        # This is how objects collaborate and pass messages to each other.
        self.engine.start()


# Step 1: Create an Engine object
my_engine = Engine(250)

# Step: Pass that Engine OBJECT into the Car class when creating the Car.
# We are literally handing the 'my_engine' object to the Car's constructor.
my_car = Car("Sports Coupe", my_engine)

# Step 3: Use the Car object. It will internally use the Engine object we gave it.
my_car.drive()



# Concept 5: CLASS ATTRIBUTES vs. INSTANCE ATTRIBUTES (BONUS FOUNDATION)
# Instance attributes (like self.name) belong to ONE specifc object.
# Class attributes belong to the CLASS ITSELF and are shared by ALL objects
# created from that class.

class Bird:
    # This is a CLASS attribute. It is defined directly in the class body.
    # Every single bird created will share this exact same value.
    species = "Aves"

    def __init__(self, name):
        # This is an INSTANCE atrribute. Unique to each individual bird.
        self.name = name


bird1 = Bird("Parrot")
bird2 = Bird("Eagle")

# Both birds share the class attribute
print(bird1.species)    # Aves
print(bird2.species)    # Aves

# But they have their own unique instance attributes
print(bird1.name)   # Parrot
print(bird2.name)   # Eagle


        