# SOLID is like a set of rules for building with LEGO blocks!

## S - Single Responsibility Principle (SRP):

Imagine you have a robot. The robot's job is to paint, not to cook or sing. Single Responsibility means each robot (or class) should have one main job, just like your toys do one thing really well.
EX - Imagine you have a toy that is a dog. The dog's main job is to bark. If you want a toy that meows, you get a cat toy. Each toy has a single responsibility—dog for barking, cat for meowing.

## O - Open/Closed Principle (OCP):

Think of a box of animal toys. Once you close the box, you don't need to change the toys inside. If you want a new animal, you just add it outside the box. The closed box (old code) doesn't change; you add new things without touching the old ones.

## L - Liskov Substitution Principle (LSP):

Imagine you have a bunch of toy cars, and you can make them go forward by pushing a button. Now, let's say you have a big toy truck. According to the Liskov Substitution Principle, you should be able to use the truck in place of a car without causing any problems.
Here's how it works:
### Using a Car:
When you push the button on a toy car, it goes forward. You expect this from all your cars.
### Using a Truck (Applying LSP):
Now, according to LSP, if you replace the car with a truck, pressing the same button should make the truck go forward as well. The truck should behave just like the car in this situation.
So, in simpler terms, the Liskov Substitution Principle says that you should be able to substitute a parent class object with an object of its child class without affecting the correctness of your program.
In our toy example, the truck can be substituted for the car because it can perform the same action (going forward with the button). This principle helps make our code more flexible and allows us to use different kinds of toys in the same situations without unexpected issues.

## I - Interface Segregation Principle (ISP):

Imagine a toy with buttons. If you only want to press one button, you don't need to see all the other buttons. Each type of toy has its set of buttons. If you only need one type of button, you don't have to deal with the ones you don't need

## D - Dependency Inversion Principle (DIP):

Think of building a tower with blocks. The top block doesn't hold the tower; it depends on the blocks below. Dependency Inversion means the higher-level things depend on the lower-level things. For example, if you have a zoo (higher level), it depends on animals (lower level). You can't have a zoo without animals.

So, SOLID is like having toys with clear roles, not changing old toys when you add new ones, making big toys do what small toys do, having only the buttons you need, and building things where each part depends on the right things below it.
