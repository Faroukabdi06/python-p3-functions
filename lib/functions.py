#!/usr/bin/env python3

def greet_programmer():
    pass
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    pass
    print(f"Hello, {name}!")
greet("farouk")

def greet_with_default(name="programmer"):
    pass
    print(f"Hello, {name}!")
greet_with_default()

def add(num1, num2):
    pass
    return num1 + num2
add(2,2)

def halve(number):
    pass
    if not isinstance(number, (int,float)):
     return None
    return number / 2
halve(4)