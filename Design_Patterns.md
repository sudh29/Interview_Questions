#Design patterns 

Design patterns are typical solutions to common problems in software design. They are like templates that can be applied to real-world programming problems.
Each pattern is a blueprint that you can customize to solve a particular design problem in your code. Here’s an overview of design patterns, their types, and examples.

## Types of Design Patterns

### Creational Patterns: Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

### Structural Patterns: Deal with object composition or the structure of classes and objects.

### Behavioral Patterns: Deal with object collaboration and how objects interact with each other.

## Common Design Patterns

### Creational Patterns

#### Singleton: Ensures a class has only one instance and provides a global point of access to it.

Example: Database connection pool.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
```

Factory Method: Defines an interface for creating an object but lets subclasses alter the type of objects that will be created.

Example: Creating different types of user notifications.

```python
class NotificationFactory:
    def create_notification(self, type):
        if type == "SMS":
            return SMSNotification()
        elif type == "Email":
            return EmailNotification()
```

Builder: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

Example: Building a complex House object with different parts.


```python
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Walls built"
    
    def build_roof(self):
        self.house.roof = "Roof built"
    
    def get_house(self):
        return self.house
```
Structural Patterns
Adapter: Allows incompatible interfaces to work together.

Example: Using different types of plugs with a standard socket.


```python
class EuropeanSocket:
    def voltage(self):
        return 230

class USASocketAdapter:
    def __init__(self, european_socket):
        self.european_socket = european_socket

    def voltage(self):
        return self.european_socket.voltage() / 2
```

Composite: Composes objects into tree structures to represent part-whole hierarchies. Allows individual objects and compositions to be treated uniformly.

Example: File system directories and files

```python
class File:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add(self, file):
        self.files.append(file)

    def display(self):
        print(self.name)
        for file in self.files:
            file.display()
```

Decorator: Adds responsibilities to objects dynamically.

Example: Adding scroll bars to a window.

```python
class Window:
    def render(self):
        print("Render window")

class ScrollDecorator:
    def __init__(self, window):
        self.window = window

    def render(self):
        self.window.render()
        self.render_scroll()

    def render_scroll(self):
        print("Render scroll")
```
Behavioral Patterns
Observer: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

Example: Event handling systems.

```python
class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def notify_all(self):
        for observer in self.observers:
            observer.update()

class Observer:
    def update(self):
        print("Observer updated")
```
Strategy: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Example: Different sorting algorithms (quick sort, merge sort).

```python
class SortStrategy:
    def sort(self, data):
        pass

class QuickSort(SortStrategy):
    def sort(self, data):
        print("Quick sort")

class MergeSort(SortStrategy):
    def sort(self, data):
        print("Merge sort")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        self.strategy.sort(data)
```

Command: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

Example: Menu items in a GUI

```python
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def execute(self):
        print("Light on")

class LightOffCommand(Command):
    def execute(self):
        print("Light off")

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
```

## Conclusion

Design patterns provide reusable solutions to common problems in software design, making it easier to manage complex systems.
By understanding and applying these patterns, developers can create more flexible, reusable, and maintainable code.
