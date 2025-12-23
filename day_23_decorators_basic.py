
"""
PYTHON DECORATORS

Real-Life Analogy
Think of a sandwich. A basic sandwich is just a bread and filling.
But you can WRAP it in paper, and label, put it in a box without
changing what the sandwich actually is.


A decorator does the same thing to function:
it WRAPS a function with extra behavior, without changing the original function.

"""

import time
from datetime import datetime


# Step 1: The problem (without decorators)

def calculate_sum(numbers):
    """ Calculate the sum of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total

print("=" * 60)
print("Step 1: Basic function (no decoration)")
print("=" * 60)

result = calculate_sum([1,2,3,4,5])
print(f"Sum: {result}")
print()


# Step 2: Adding timing (The Messy Way)


def calculate_sum_with_timing(numbers):
    """
    Now we want to measure how long this takes.
    We have to add timing code INSIDE the function
    This mixes timing logic with calculation logic.
    """

    start_time = time.time()     # Record start time

    # The actual calculation (same as before)
    total = 0
    for num in numbers:
        total += num

    end_time = time.time()  # Record end time
    elapsed = end_time - start_time

    print(f"    Funtion took {elapsed:.6f} seconds")
    return total

print("=" * 60)
print("Step 2: The messy way (timing code mixed in)")
print("=" * 60)

result = calculate_sum_with_timing([1,2,3,4,5])
print(f"Sum: {result}")
print()

# PROBLEM: If we want to time 10 different functions,
# we have to add this timing cosw to all of them!



# Step 3: Building a Timing Decorator


def time_it(func):
    """
    A decorator that measures how long a function takes to run.

    HOW IT WORKS:
    1. Takes a function as input
    2. Creates a wrapper that adds timing around it
    3. Returns the wrapper
    """

    def wrapper(*args, **kwargs):
        """
        This wrapper runs the timing logic.


        *args, **kwargs means:
        "Accept any number of positional or keyword arguments"
        So this decorator works with ANY function signature.
        """

        # BEFORE: Start the timer
        start_time = time.time()

        # EXECUTE: Call the original function with its arguments
        result = func(*args, **kwargs)

        # AFTER: Stop the timer and print elapsed time
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"    {func.__name__}() took {elapsed:.6f} seconds")

        # Return the original result
        return result
    return wrapper

print("-" * 80)
print("Step 3: Using the timing decorator")
print("=" * 80)


@time_it
def calculate_sum_decorated(numbers):
    """
    Same calculation function, but now decorates with @time_it.
    The function itself is clean - no timing code inside!
    """
    total = 0
    for num in numbers:
        total += num
    return total


# Test with a larger dataset to see timing in action
numbers = list(range(1, 1000001))     # 1 million numbers
result = calculate_sum_decorated(numbers)
print(f"Sum: {result}")
print()



