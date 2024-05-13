import json

def convert_to_milligrams(input_str):
    output = {}
    items = input_str.split(', ')
    for item in items:
        key, value = item.split()
        value_num, unit = int(value[:-1]), value[-1]
        if unit == 'g':
            value_num *= 1000  # Convert grams to milligrams
        if key in output:
            output[key].append(f"{value_num} mg")
        else:
            output[key] = [f"{value_num} mg"]
    return output

input_str = "ABC 1g, XYZ 5g, ABC 20g"
output_json = convert_to_milligrams(input_str)
print(output_json)

# Flattening the output dictionary to a list of key-value pairs
output_list = [f'"{key}": "{value}"' for key, values in output_json.items() for value in values]
print(output_list)
# Joining the list elements with comma and curly braces to form a JSON-like string
output_str = "{" + ", ".join(output_list) + "}"
print(output_str)


# Duck typing in python
'''
Duck typing is a concept in programming languages like Python where the type or class of an object is less important than the methods it defines.
In essence, if an object behaves like a duck (i.e., it quacks like a duck and walks like a duck), then it is considered a duck, regardless of its 
actual type.

In Python, this means that you can use an object if it supports the methods or operations you intend to perform on it, without necessarily checking
its type explicitly. This promotes flexibility and allows different objects to be used interchangeably based on their behavior rather than their type.

Here's a simple example of duck typing in Python:
'''

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(obj):
    obj.quack()

# Both Duck and Person classes have a quack method
duck = Duck()
person = Person()

# Passing Duck object to make_it_quack
make_it_quack(duck)  # Output: Quack!

# Passing Person object to make_it_quack
make_it_quack(person)  # Output: I'm quacking like a duck!

```
'''
In this example, we have a Duck class and a Person class, both of which have a quack method. The make_it_quack function takes an object
and calls its quack method. Even though duck and person are instances of different classes, they can both be passed to make_it_quack 
because they both have the necessary quack method. This demonstrates the principle of duck typing in Python.
'''

