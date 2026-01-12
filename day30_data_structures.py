"""
Python Data Structures Refrence Guide
A comprehensive demonstration of core data structures and their operations


"""

# PART 1: Ordered, Mutable Collections


def demonstrate_lists():
    """
    Lists are ordered, mutable sequences that can contain mixed types.
    Best for: ordered data, frequent modifications, stack/queue operations

    """
    print("\n==== LISTS ====")

    # Creation 
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    empty = []

    # Adding elements 
    numbers.append(6)       # Add to end: O(1)
    numbers.insert(0, 0)    # Insert at index: (0)
    numbers.extend([7, 8, 9])   # Add multiple: O(k)


    # Accessng elements
    first = numbers[0]          # Index access: O(1)
    last = numbers[-1]          # Negative indexing: O(1)
    slice_result = numbers[2:5] # Slicing: O(k)

    # Modifying elements 
    numbers[0] = 10             # Update by index: O(1)


    # Removing elements 
    numbers.pop()           # Remove last: O(1)
    numbers.pop(0)          # Remove by index: O(n)
    numbers.remove(3)        # Remove by value: O(n)


    # Searching and counting
    position = numbers.index(4)     # Findex: O(n)
    count = numbers.count(5)        # Count occurences: O(n)
    exists = 5 in numbers           # Membership test: O(n)

    # Sorting and reversing
    numbers.sort()                  # In-place sort: O(n log n)
    numbers.reverse()                # In-place reverse: O(n)
    sorted_copy = sorted(numbers)     # Return sorted copy: O(n log n)

    # Useful operations
    length = len(numbers)           # Get length: O(1)
    numbers.clear()                   # Remove all elements: O(n)

    print(f"List operations completed. Final sorted copy: {sorted_copy}")




# PART 2: TUPLES - Ordered, Immutable Collections


def demonstrate_tuples():
    """
    Tuples ore ordered, immutable, suquences.
    Best for: fixed collections, dictionary keys, function  return values

    """

    print("\n=== TUPLES ===")

    # Creation
    coordinates = (10, 20)      
    single = (42,)          # Single element needs comma
    mixed = (1, "text", 3.14)
    unpacking = 1, 2, 3         # Parentheses optional


    # Accessing elements 
    x = coordinates[0]      # Index access: O(1)
    y = coordinates[-1]     # Negative indexinf: O(1)

    # Unpacking 
    a, b = coordinates         # Tuple unpacking
    first, *rest = (1, 2, 3, 4)     # Extended unpacking


    # Operations (limited due to immutability)
    count = mixed.count(1)      # COunt occurences: O(n)
    position = mixed.index("text")  # Find index: O(n)
    exists = 3.14 in mixed          # Membership test: O(n)

    # Concatenation (creates new tuple)
    combined = coordinates + (30, 40)       # O(n + m)
    repeated = coordinates * 3                 # O(n * k)

    # Use case: multiple return values
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers)
    
    min_val, max_val, total = get_stats([1,2,3,4,5])

    print(f"Tuple unpacking result: min={min_val}, max={max_val}, total={total}")



# PART 3: SETS - Unordered, Unique Collections


def demonstrate_sets():
    """
    Sets are unordered collections of unique elements.
    Best for: uniqueness, membership testing, mathematical set operations
    
    """

    print("\n=== SETS ===")

    # Creation 
    numbers = {1,2,3,4,5}
    duplicates = {1,2,3,3,2}        # Automatically removes duplicates
    from_list = set([1,2,3])        # Convert from list
    empty = set()                   # Note: {} creates empty dict!


    # Adding elements
    numbers.add(6)                  # Add single element O(1)
    numbers.update([7, 8, 9])       # Add multiple: O(k)

    # Removing elements 
    numbers.remove(9)           # Remove (raises error if absent)
    numbers.discard(1100)       # Remove (no error if absent): O(1)
    popped = numbers.pop()      # Remove arbitrary element: O(1)


    # Membership testing (very fast!)
    exists = 5 in numbers       # Membership test: O(1)


    # Set operations
    set_a = {1,2,3,4,5}
    set_b = {4,5,6,7,8}


    union = set_a | set_b           # Union: O(len(set_a) + len(set_B))
    intersection = set_a & set_b    # Intersection: o(min(len(set_a), len(set_b)))
    difference = set_a - set_b       # Difference: O(len(set_a))
    symmetric_diff = set_a ^ set_b   # Symmetric difference


    # Set relationships
    is_subset = {1,2} <= set_a    # Subset test
    is_superset = set_a >= {1,2}  # SUperset test
    is_disjoint = set_a.isdisjoint(10,11)   # No common elements

    # Practical use case: finding duplicates
    def find_duplicates(items):
        seen = set()
        duplicates = set()
        for item in items:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)

            return duplicates
        
    dupes = find_duplicates([1,2,3,2,4,3,5])
    print(f"Set operations - Union: {union}, Intersection: {intersection}")
    print(f"Found duplicates: {dupes}")