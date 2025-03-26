
import math  # import keyword
from random import randint  # from keyword

def keywords():
    """Function to demonstrate Python keywords"""
    
    # Logical operations: and, or, not
    a, b = True, False
    print("Logical Operations:", a and b, a or b, not b)
    
    # Conditional Statements: if, elif, else
    x = randint(0, 10)
    if x > 5:
        print("x is greater than 5")
    elif x == 5:
        print("x is exactly 5")
    else:
        print("x is less than 5")
    
    # Looping: for, while, break, continue, pass
    for i in range(5):
        if i == 2:
            continue  # Skip 2
        if i == 4:
            break  # Stop at 4
        print("For loop iteration:", i)
    
    count = 0
    while count < 3:
        print("While loop count:", count)
        count += 1
        if count == 2:
            pass  # Placeholder statement
    
    # Function Definition: def, return
    def square(num):
        return num * num
    print("Square of 4:", square(4))
    
    # Exception Handling: try, except, finally, raise
    try:
        y = 10 / 0
    except ZeroDivisionError as e:
        print("Caught an exception:", e)
    finally:
        print("This block always executes.")
    
    # Assertions: assert
    assert 2 + 2 == 4, "Math is broken!"
    
    # Class and Object: class
    class Demo:
        def __init__(self, name):
            self.name = name
    obj = Demo("Python")
    print("Object name:", obj.name)
    
    # Working with None
    value = None
    if value is None:
        print("Value is None")
    
    # Global and nonlocal variables
    global_var = "I am global"
    
    def outer_function():
        nonlocal_var = "Outer"
        
        def inner_function():
            nonlocal nonlocal_var
            nonlocal_var = "Modified"
            print("Nonlocal variable:", nonlocal_var)
        
        inner_function()
    
    outer_function()
    
    # Using lambda
    double = lambda x: x * 2
    print("Double of 5:", double(5))
    
    # Using with statement
    with open("example.txt", "w") as file:
        file.write("Using 'with' statement")
    
    # Using yield
    def generator():
        for i in range(3):
            yield i
    print("Generated values:", list(generator()))
    
    print("All keywords used successfully!")

# Execute demonstration
if __name__ == "__main__":
    keywords()
