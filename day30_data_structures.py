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
    is_disjoint = set_a.isdisjoint({10,11})   # No common elements

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



# PART 4: DICTIONARIES - Key-Value Mappings


def demonstrate_dictionaries():
    """
    Dictionaries are unordered collection of key-value pairs.
    Best for: lookups, counting, caching, configuration
    """

    print("\n=== DICTIONARIES ===")


    # Creation
    person = {"name": "Alice", "age": 30, "city": "Berlin"}
    empty = {}
    from_pairs = dict([("a", 1), ("b", 2)])
    dict_comp = {x: x**2 for x in range(5)}     # Dictionary comprehension


    # Accessing elements 
    name = person["name"]       # Direct access: O(1), raises KeyError if missing
    age = person.get("age")     # Safe access: O(1), returns None if missing
    age = person.get("height", 0)   # With default value

    # Adding/Updating elements
    person["job"] = "Engieer"       # Add new key: O(1)
    person["age"] = 1               # Update existing: O(1)
    person.update({"city": "Munich", "country": "Germany"})     # Bulk update


    # Removing elements
    job = person.pop("job")     # Remove and return: O(1)
    person.pop("missing", None) # Safe removal with dafault, if "missing" it returns None
    city = person.popitem()      # Remove arbitrary item(random removal O(1)
   

    # Membership testing
    has_name = "name" in person       # Check key existence: O(1)
    has_value = "Alice" in person.values()      # Check value: O(n)


    # Iteration
    for key in person:      # iterate over keys
        print(f"{key}: {person[key]}")

    for key, value in person.items():       # Iterate over key-value pairs
        print(f"{key} = {value}")

    # Dictionary views
    keys = person.keys()        # Get all keys
    values = person.values()    # Get all values
    items = person.items()      # Get key-value pairs


    # Useful methods
    person.setdefault("age", 25)        # Set if not exists: O(1)
    merged = {**person, **{"hobby": "coding"}}      # Dictionary unpacking

    # Practical use case: counting
    def count_words(text):
        counts = {}
        for word in text.split():
            counts[word] = counts.get(word, 0) + 1
        return counts
    word_counts = count_words("hello world hello python world")
    print(f"Word counts: {word_counts}")


    # defaultdict and Counter alternatives
    from collections import defaultdict, Counter

    freq = defaultdict(int)         # Auto-initializes to 0
    freq["a"] += 1


    counter = Counter("hello world")        # Specialized for counting
    most_common = counter.most_common(2)

    print(f"Most common characters: {most_common}")


# PART 5: STRINGS - Immutable Character Sequences


def demonstrate_strings():
    """
    Strings are immutable sequences of characters.
    Best for: text processing, manuipulation, pattern matching

    """

    # Creation
    text = "Hello! World"
    multiline = """This is a
    multiline string """
    raw = r"C:\new\path"                # Raw string (no escape processing)

    # Accessing elements
    first = text[0]             # Index access: O(1)
    last = text[-1]             # Negative indexing: O(1)
    sunstring = text[0:5]       # Slicing: O(k)

    # String methods (all create new strings - immutable)
    upper = text.upper()        # Convert to uppercase: O(n)
    lower = text.lower()        # Convert to lowercase: O(n)
    stripped = "    hello   ".strip()       # Remove whitspace O(n)
    replaced = text.replace("World!", "Python")     # Replace substring: O(n)

    # Splitting and joining
    words = text.split(", ")    # Split by delimiter: O(n)
    joined = "-".join(words)    #Join with sepertor: O(n)

    # Searching
    index = text.find("World")      # Find substring: O(n), returns -1 if not found
    index = text.index("World")     # Find substring: O(n), raises ValueError if not found
    starts = text.startswith("Hello")   # Check prefix: O(k)
    ends = text.endswith("!")           # check suffix: O(k)
    contains = "Worlds" in text          # Membership test O(n)

    # Checking properties
    is_alpha = "abc".isalpha()      # All alphabetic
    is_digit = "123".isdigit()      # All digits
    is_alnum = "acx23".isalnum()    # Alphanumeric
    is_space = "   ".isspace()      # All whitespace


    # Formatting
    name = "Nikhil"
    age = 27

    # Old style
    old_format = "Name: %s, Age: %d" % (name, age)

    # .format() style
    new_format = "Name: {}, Age: {}".format(name, age)
    named_format = "Name: {n}, Age: {a}".format(n=name, a=age)

    # f-strings (Python 3.6, preferred)
    f_string = f"Name: {name}, Age: {age}"
    expression = f"Next year: {age + 1}"

    # String building 
    parts = []
    for i in range(5):
        parts.append(f"Item {i}")
    result = " ".join(parts)        # More efficient than += in loop

    print(f"String formatting: {f_string}")
    print(f"Built string: {result}")



# PART 6: DEQUE - Double Ended Queue

def demonstrate_deque():
    """
    Deque (from collections) is optimized for fast operations on both ends.
    Best for: queues, sliding windows, undo operations
    """

    print("\n=== DEQUE ===")

    from collections import deque

    # Creation
    dq = deque([1, 2, 3])
    bounded = deque(maxlen=3)       # Fixed-size, auto-removes oldest

    # Adding elements (both ends - O(1))

    dq.append(4)            # Add to right
    dq.appendleft(0)        # Add to left
    dq.extend([5,6])        # Add multiple to right
    dq.extendleft([-2, -1]) # Add multiple to left (reversed)

    # Removing elements (both ends - O(1))
    right = dq.pop()        # Remove from right
    left = dq.popleft()     # Remove from left

    # Rotation
    dq.rotate(1)            # Rotate right: O(k)
    dq.rotate(-1)           # Rotate left: O(k)

    # Other operations
    dq.reverse()            # Reverse in-place: O(n)
    count = dq.count(2)      # Count occurences: O(n)

    # Practical use case: sliding window maximum
    def sliding_window_max(nums, k):
        dq = deque()
        result = []


        for i, num in enumerate(nums):
            # Remove elements outside window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
    
    print(f"Deque contents: {list(dq)}")


# PART 7: HEAPQ - Prioritu Queue

def demonstrate_heapq():
    """
    heapq implements a min-heap (priority queue).
    Best for: finding smallest/largest items, priority scheduling
    """

    print("\n=== HEAPQ ===")

    import heapq

    # Creation (heapify existing list)
    numbers = [5, 2, 8, 9, 3]
    heapq.heapify(numbers)
    heapq.heappush(numbers, 4)       # Push element: O(log n)

    # Removing elements (always removes smallest)
    smallest = heapq.heappop(numbers)   # Pop smallest: O(log n)

    # Peek at smallest (without removing)
    peek = numbers[0]       # O(1)

    # Push and pop in one operation
    replaced = heapq.heappushpop(numbers, 6)    # O(log n)
    replaced = heapq.heapreplace(numbers, 7)   # O(log n)

    # Find n larges/smallest 
    data = [1, 8, 2, 9, 3, 7, 4, 6, 5]      
    smallest_3 = heapq.nsmallest(3, data)    # O(n log k)
    largest_3 = heapq.nlargest(3, data)

    # With key function
    people = [("Alice", 30), ("Bob", 25), ("Nikhil", 27)]
    oldest_2 = heapq.nlargest(2, people, key=lambda x: x[1])

    print(f"Heap smallest: {smallest}")
    print(f"Largest 3: {largest_3}")
    print(f"Oldest 2: {oldest_2}")


# PART 8: COMPREHENSIONS - Concise Collections Creation

def demonstrate_comprehensions():
    """
    Comprehensions provide concise syntax for creating collection.
    Best for: transforming data, filtering, mapping operations
    """
    print("\n=== COMPREHENSIONS ===")


    # List comprehension
    squares = [x**2 for x in range(10)]
    evens = [x for x in range(10) if x % 2 == 0]

    # Nested list comprehension
    matrix = [[i*j for j in range(3)] for i in range(3)]
    flatenned = [item for row in matrix for item in row]

    # Set comprehension
    unique_squares = {x**2 for x in [1,-1,2,-2,3]}

    # Dictionary comprehension
    square_dict = {x: x**3 for x in range(5)}
    inverted = {v:k for k, v in square_dict.items()}

    # Generator expression (memory efficient)
    gen = (x**2 for x in range(100000))     # doesn't create list
    first_gen = next(gen)

    # Conditional comprehension
    categorized = ["even" if x % 2 == 0 else "odd" for x in range(5)]

    print(f"Squares: {squares}")
    print(f"Matrix: {matrix}")
    print(f"Inverted dict: {inverted}")




# MAIN DEFINITION


def main():
    """
    Execute all demonstration to showcase Python data structures.
    
    """
    print("=" * 80)
    print("PYTHON DATA STRUCTURES ")
    print("=" * 80)

    demonstrate_lists()
    demonstrate_tuples()
    demonstrate_sets()
    demonstrate_dictionaries()
    demonstrate_strings()
    demonstrate_deque()
    demonstrate_heapq()
    demonstrate_comprehensions()

    print("\n" + "=" * 80)
    print("ALL demonstration completed")
    print("=" * 80)


if __name__ == "__main__":
    main()

