
"""
PYTHON OS LIBRARY & FILE HANDLING 

This program teaches you foundational concepts about:
- What inbuilt libraries are and why we use them
- Absolute vs relative paths
- Checking existence of files and directories 
- Distinguishing between files and directories
- Exception handling for file operations

Each section includes:
1. Conceptual explaination
2. Working code examples
3. Comments explaining WHY, not just HOW

"""


# SECTION 1: WHAT is an inbuilt (built-in) library and why use it ?

"""
A library is a collection of pre-written code that solves problems.
Python comes with many "built-in" libraries (also called "standard library")

Why use libraries?
1. Avoid reinventing the wheel - Someone already solved this problem
2. Tested and reliable - These libraries are used by millions of developers.
3. Save time - Focus on your problem, not basic file operations.
4. Cross platform - Works on Windows, Mac, Linux with same code.


The 'os' library specifcally helps us interact with the operating system:
- Navigate file systems
- Check if files exist
- Create/delete folders
- Get file information
- Work with paths in a way that works across different operating systems.


"""

# This is how we IMPORT a library - bringing its functionality into our programs.
# We are importing 'os'because we want to interact with the operating system



import os

print("=" * 80)
print("SECTION 1: Understanding Inbuilt Libraries")
print("=" * 80)
print("\n We imported the 'os' library sucessfully")
print(" This gives us acess to 150 functions for file/directory operations")
print(" Without 'os' we would have to write these functions ourselves (thousands of lines)")
print("\n")


# SECTION 2: ABSOLUTE vs RELATIVE PATHS - The foundation of File Navigation

"""
What is a PATH?

A path is the ADDRESS of a file or folder on your computer.
Think of it like a street address - it tells the computer WHERE to find something.

There are TWO types of paths:


1. ABSOLUTE PATH (Complete Address)
    - Starts from the ROOT of your file system
    - Complete, unambiguous location
    - Works from ANYWHERE on your computer
    - Example (Windows): C:\\Users\\YourName\\Documents\\file.txt
    - Example (Mac/Linux): /home/username/Documents/file.txt

2. RELATIVE PATH
    - Starts from your CURRENT working directory
    - Like saying "go to the folder next to me"
    - Shorter and more portable
    - Example: ./data/file.txt (.means "current directory")
    - Example: ../file.txt (.. means "parent directory")

    
WHY DOES THIS MATTER?
- Absolute paths are specific to YOUR computer
- Relative paths work when you share code with others
- Understanding this prevent "File not found" errors


"""

print("=" * 80)
print("SECTION 2: Absolute vs Relative Paths")
print("=" * 80)


# os.getcwd() returns the CURRENT WORKING DIRECTORY
# This is WHERE your Python script thinks it is right now
# It's like asking "Where am i standing right now?"
current_directory = os.getcwd()
print(f"\n Current Working Directory (WHERE WE ARE):")
print(f" {current_directory}")
print(f" ^ This is an ABSOLUTE path - complete adress from the root")

# Let's demonstrate the difference with examples
print("\n" + "-" * 80)
print("EXAMPLES:")
print("-" * 80 )


# Example 1: Absolute path 
# This is the FULL address to a file - starts from the root of the filesystem
# On Windows: starts with C:\ or D:\
# On Mac/Linux: starts with /

example_absolute = os.path.join(current_directory, "example_file.txt")
print(f"\n1. ABSOLUTE PATH:")
print(f" {example_absolute}")
print(" Why use this? It works from ANYWHERE on your computer")
print(" Downside? It's specific to YOUR computer's structure")


# Example 2: Relative path
# This is a path RELATIVE to where we currently are
# ./ means "in the current directory"

example_relative = "./example_file.txt"
print(f"\n2. RELATIVE PATH:")
print(f" {example_relative}")
print(" Why use this? It's portable - works when you share code")
print(" Downside? It depends on WHERE you run the scripr from")


# Example 3: Parent directory
# ../ means "go UP one level" (to the parent folder)
example_parent = "../example_file.txt"
print(f"\n3. PARENT DIRECTORY PATH:")
print(f"  {example_parent}")
print(" Why use this? To access files OUTSIDE your current folder")


print("\n" + "=" * 80)
print("KEY INSIGHT: Most projects use RELATICE paths for portability")
print("=" * 80)



# SECTION 3: CHECKING IF FILES AND FOLDERS EXIST - Avoiding Errors



"""
Why check if something exists?

Before trying to open a file or enter a directory, you should check if it exists.
This is like knocking on a door before entering - it prevents errors.


WHY IS THIS IMPORTANT?
1. Prevents crashes - your program won't crash with "FileNotFoundError"
2. Better user experience - you can give helpful error messages
3. Logic flow - you can create files if they don't exist, or skip if they do
4. Debugging - helps you understand what went wrong

Python gives us simple functions to check existence:
- os.path.exists() - returns True if ANYTHING (file of folder ) exists
- os.path.isfile() - returns if it's specifically a FILE
- os.path.isdir() - returns True if it's specifically a DIRECTORY

"""

print("=" * 80)
print("SECTION 3: Checking Existence of Files and Folders")
print("=" * 80)


# Let's create a test file to demonstrate
# We will use this file to show how existence checking works
test_file_path = "test_example.txt"
test_dir_path = "test_directory"

# First, let's check if our test file already exists
# This prevents accidentally overwriting existing files
print(f"\n Checking if '{test_file_path}' exists...")

if os.path.exists(test_file_path):
    print(f" File already exists - We will use it for demonstration")
else:
    print(f" File doesn't exist yet - let's create it")
    # The 'with' statement automaticallu closes the file when done
    # This SAFER than manually opening/closing
    # 'w' mode means WRITE - creates file if it doesn't exist
    with open(test_file_path, 'w') as f:
        # We are writing content so the file isn't empty
        # This makes it easier to verify later
        f.write("This is a test file for learning OS library concepts.\n")
        f.write("Created for educational purposes.")
    print(f" Created file sucessfully")

    
print("\n" + "=" * 80)
print("DEMONSRATION: Different existence checking methods")
print("-" * 80)


# Method1: os.path.exists() - Most general check
# Returns True for BOTH files and directories
# Use this when you don't care whether it's a file or folder
print(f"\n1. os.path.exists('{test_file_path}')")
exists = os.path.exists(test_file_path)
print(f" Result: {exists}")
print(f" Meaning: Something (file or directory) exists at theis path")


# Method 2: os.path.isfile() - Specifically check for FILES
# Returns True if it's a file (not a directory)
# Use this when you are about to READ or WRITE to a file

print(f"\n os.path.isfile('{test_file_path}')")
is_file = os.path.isfile(test_file_path)
print(f" Result: {is_file}")
print(f" Meaning: This is specifically a FILE (not a folder)")
print(f" Use case: Before reading file contents")


# Method 3: os.path.isdir() - Specifically checks for DIRECTORIES
# Returns True ONLY if it's a directory (not a file)
# Use this when you are about to list contents or navigate into a folder
print(f"\n3. os.path.isdir('{test_file_path}')")
is_dir = os.path.isdir(test_file_path)
print(f" Result: {is_dir}")
print(f" Meaning: This is NOT a directory (its a file)")


# Now let's create a directory to show the difference
print(f"\n" + "-" * 80)
print(f"Creating a directory for comparison")
print("-" * 80)


# os.makedirs() Creates a directory
# exist_ok=True means "don't crash if it already exists"
# This is safer than checking existence first
os.makedirs(test_dir_path, exist_ok=True)
print(f" Created/verified directory: {test_dir_path}")

# Now let's compare the same checks on a  DIRECTORY
print(f"\n Comparing checks on DIRECTORY '{test_dir_path}':")
print(f" os.path.exists(): {os.path.exists(test_dir_path)}")
print(f" os.path.isfile(): {os.path.isfile(test_dir_path)}")
print(f" os.path.isdir(): {os.path.isdir(test_dir_path)}")

print("\n" + "=" * 80)
print("KEY INSIGHT: Always check existence before operations to prevent errors")
print("\n")


# SECTION 4: Distinguishing files from directories - why it matters

"""
You cannot:
- read the contents of a directory like a text file
- list the contents of a file like a directory
- do the same operations on both


This is like trying to:
- read a folder like a book (doesn't work)
- look inside a document for more documents (doesn't work)


PRACTICAL IMPLICATIONS:
1. before reading, confirm it's a FILE
2. before listing contents, confirm it's a DIRECTORY
3. before processing, know what you are dealing with


Real-world analogy:
- File = a single document
- Directory = a filing cabinet that contains documents

"""


print("=" * 80)
print("Section 4: File vs Directory - Understanding the difference")
print("=" * 80)


# Let's create a practical function what something is
# This demonstrates a commpn pattern in real programs

def identify_path_type(path):
    """
    Identifies whether a path is a file, directory, or doesn't exist.

    WHY THIS FUNCTION?
        - combines multiple checks in a reusable way
        - provides clear, human-readable output
        - demonstrates defensive programming (checking existence first)

    Args:
        - path: the path to check(string)

    Returns:
        - a string describing what the path is
    """

    # First, check if ANYTHING exists at this path
    # If nothing exists, the other checks are meaningless
    if not os.path.exists(path):
        return "Does not exist"
    
    # If we got here, SOMETHING exists
    # Now determine id it's a file or directory
    elif os.path.isfile(path):
        return "File"
    elif os.path.isdir(path):
        return "Directory"
    else:
        # On some systems, there are special file types (links, devices, etc.)
        # This catches those rare cases
        return "Special file type"
    

# Now let's test our function on different paths
print("\n Testing path identification: ")
print("-" * 80)


# Test 1: Out test file
result1 = identify_path_type(test_file_path)
print(f"\n {test_file_path}")
print(f" Type: {result1}")
print(f" What you CAN do: Open it, read its contents, write to it.")
print(f" What you CANNOT do: List files inside it")

# Test 2: Our test directory
result2 = identify_path_type(test_dir_path)
print(f"\n {test_dir_path}:")
print(f" Type: {result2}")
print(f" What you CAN do: List contents, create files inside it ")
print(f" What you CANNOT do: Read it like a text file")

# Test 3: Something that doesn't exist
nonexistent = "this_does_not_exist.txt"
result3 = identify_path_type(nonexistent)
print(f"\n {nonexistent}")
print(f" Type: {result3}")
print(f" What happens if you try to open it? FileNotFoundError")



# Section 5: Exception Handling: Dealing with reality
"""
What are exceptions and why handle them?

An EXCEPTION is Python's way of saying "I can't do what you asked"
Think of it like error message in real life:
- "File not found" - the file doesn't exist
- "Permission denied" - you are not allowed to access this
- "Directory not empty" - can't delete a folder with files in it

WHY HANDLE EXCEPTIONS?
1. Prevent crashes - your program keeps running even when errors occur
2. User friendly - give helpful messages intead of cryptic errors
3. Grateful degradation - the program can continue with other tasks
4. Debugging - you can log errors and understand what went wrong

COMMON FILE-RELATED EXCEPTION:
1. FileNotFoundError - File/directory doesn't exist 
2. PermssionError - Insufficient permission to access
3. IsADirectoryError - tried to open a directory as a file
4. NotADirectoryError - tried to list contents of a file
5. OSError - general operating system related errors

THE TRY-EXCEPT PATTERN:
try:
    # Code that MIGHT fail
except SpecificError:
    # What to do if it DOES fail


"""

print("=" * 80)
print("SECTION 5: Exception Handling - Dealing with Errors Gracefully")
print("=" * 80)

# Example 1: FileNotFoundError
print("\n" + "-" * 80)
print("EXAMPLE 1: FileNotFoundError - When files dont't exist")
print("-" * 80)

def demonstrate_file_not_found():
    """
    Shows how FileNotFoundError occurs and how to handle it.

    What causes this?
        - trying to open a file that doesn't exist
        - typo in the filename
        - file was moved or deleted


    How to prevent?
        - check existence with os.path.exists() first
        - Use try-except to catch the error
    """
    nonexistent_file = "this_definitely_does_not_exist.txt"

    print(f"\n Attempting to read '{nonexistent_file}'...")

    try:
        # This will fail because the file doesnot exist
        # The 'try' block lets us attempt it safely
        with open(nonexistent_file, 'r') as f:
            content = f.read()
        print("Sucess") # This line will never execute

    except FileNotFoundError:
        # Python jumps here when FileNotFoundError occurs
        # Now we can provide a helpful message instead of crashing
        print("x Error caught: File doess not exist")
        print(" Solution: Check the filename or create the file first")
        print(" Program continues running")



