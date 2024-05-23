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

# CAP
'''
The CAP theorem, also known as Brewer's theorem, states that in a distributed computer system, it is impossible to simultaneously guarantee all of the
following three properties:

Consistency: Every read receives the most recent write or an error. In other words, all nodes in the system have the same data at the same time.

Availability: Every request receives a response, without guarantee that it contains the most recent write. In other words, the system continues
to operate even if some nodes fail.

Partition tolerance: The system continues to operate despite arbitrary message loss or failure of part of the system.

The CAP theorem implies that in the presence of a network partition (i.e., when some nodes are isolated from each other), a distributed system 
can either maintain consistency or availability, but not both simultaneously. It's important to note that the CAP theorem doesn't imply that you 
must choose only two out of the three properties; rather, it states that in the presence of network partitions, you must prioritize between consistency 
and availability.

In real-world scenarios, distributed systems often opt for partition tolerance and make trade-offs between consistency and availability based on
the specific requirements of the application. Different systems may prioritize consistency or availability depending on factors such as the nature 
3of the data, the use case, and the tolerance for stale or inconsistent data.
'''


class BandwidthManager:
    '''
    The BandwidthManager class should have the following methods:
    __init__(self, max_bandwidth): This constructor should take a parameter max_bandwidth (in Mbps) that represents the maximum allowed bandwidth.
    monitor_usage(self, data_size): This method should take a parameter data_size (in bytes) that represents the amount of data transferred. It should update the current bandwidth usage and return the current usage as a percentage of the maximum allowed bandwidth.
    '''
    
    def __init__(self, max_bandwidth):
        self.max_bandwidth = max_bandwidth
        self.current_bandwidth = 0
        
    def monitor_usage(self, data_size):
        self.current_bandwidth += data_size
        return (self.current_bandwidth / self.max_bandwidth) * 100


class InternetThrottler(BandwidthManager):
    '''
    The InternetThrottler class should inherit from BandwidthManager and have the following additional method:
    throttle(self): This method should be called when the current bandwidth usage exceeds the maximum allowed bandwidth. It should implement a throttling mechanism (e.g., sleep for a certain amount of time) to limit the data transfer rate.
    '''
    
    def throttle(self):
        if self.current_bandwidth > self.max_bandwidth:
            print("Throttling in effect")
        else:
            print("Not throttling")


class NetworkMonitor(BandwidthManager):
    '''
    The NetworkMonitor class should also inherit from BandwidthManager and have the following additional method:
    log_usage(self, usage_percentage): This method should take a parameter usage_percentage (a float representing the current bandwidth usage percentage) and log the usage information to a file or console.
    '''
    
    def log_usage(self, usage_percentage):
        print(f"Current log_usage usage percentage: {usage_percentage:.2f}%")

# Example usage of the InternetThrottler and NetworkMonitor classes
network_monitor = NetworkMonitor(1000)
print("Maximum allowed bandwidth:", network_monitor.max_bandwidth)

for i in range(10):
    current_usage_percentage = network_monitor.monitor_usage(100)
    print("Current usage percentage:", current_usage_percentage)
    network_monitor.log_usage(current_usage_percentage)

internet_throttler = InternetThrottler(1000)
for i in range(5):
    current_usage_percentage = internet_throttler.monitor_usage(300)
    print("Current usage percentage:", current_usage_percentage)
    internet_throttler.throttle()
