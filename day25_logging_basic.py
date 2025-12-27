
"""
LOGGING AS A SYSTEM SKILL
==========================

What you will learn:
- Why print() is insufficient for real systems
- What logging conceptually represents
- Log levels and when to use them
- Basic logging configuration
- Logging errors with full exception details


Core mental model:
Logging is writing a narrative od what your program does for FUTURE readers.
Those readers might be:
- You, debugginh at 2 AM
- A teammate investigating production issues
- An automated monitoring system
- Audit requirements

print() is for IMMEDIATE human consumption.
logging is for RECORDED system behavior.

Read this thinking: "I am learning to make my code observable."

"""


import logging
import sys
from datetime import datetime

# Part 1: Why print() is not enough

"""
print() is great for:
- quick debugging during developmemt
- direct user interaction (CLI tools)
- learnin/teaching

print() is TERRIBLE for:
- production systems
- multi-user applications
- anything that runs attended
- systems that need debugging after the fact

why?
1. output disappears (no record)
2. can't filter by severity
3. can't rout to different destinations (files, services, etc.)
4. mixes with actual program output
5. no timestamp or context
6. can't turn on/off without code changes

"""


def demonstrate_print_limitation():
    """
    Shows why print() fails in real scenarios.

    Imagine this code running on a server. Someone reports a bug.
    You need to know what happened. But...

    """
    print("\n--- LIMITATIONS OF PRINT() ---")

    # Scenario: Processing user uploads
    files = ['documents.pdf', 'photo.jpg', 'data.csv', 'corrupted.dat']

    for filename in files:
        print(f"Processing {filename}") # When did this happen ?

        # Simulate processing
        if 'corrupted' in filename:
            print("ERROR: File is corrupted" )      # How severe?  Is it critical ?
        else:
            print(f"Sucess: {filename} processed")   # where did output go ?

    print("\nProblems with this approach:")
    print("1. No timestamps - when did errors occur?")
    print("2. No severity - is 'ERROR' critical or just a warning? ")
    print("3. No persistence - output disappears after run")
    print("4. No context - which user? which server?")
    print("5. Can't filter - all or nothing")
    print("6. Mixes with real output - hard to parse")


# Part 2: What is logging? (conceptual foundation)

"""
Logging is creating a persistent, structured record od program behavior.

Think of it like a ship's log or flight recorder:
- records what happened
- records when it happened
- records severity (routine vs emergency)
- survives the 'crash'
- can be analyzed later


In code, logging means:
- using a logging library instead of print()
- categorizing messages by severity
- including context (timestamps, source, etc.)
- routing messages to appropiate destinations

"""


def demonstrate_basic_logging():
    """
    Shows the simples logging usage

    logging.basicConfig() is the minimal setup.
    After that, you get a logger that works much better than print()

    """

    print("\n--- BASIC LOGGING DEMONSTRATION---")

    # Configure logging (do this ONCE at program start)
    logging.basicConfig(
        level=logging.DEBUG,    # Show all messages 
        format='%(asctime)s - %(levelname)s - %(message)s'
        # Format: timestamp - severity - message
    )


    # Get a logger
    logger = logging.getLogger(__name__)

    # Now use it instead of print()
    logger.debug("This is a debug message.")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

    print("\nNotice:")
    print("- Each message has a timestamp")
    print("- Each message has a severity level")
    print("- Format is consistent")





    # Part 3: Log levels - the severity scale

    """
    Log levels let you categorize message severity.

    Think of them like alert systems:
    - DEBUG: Technical details for diagnosing problems (like car's diagnostic codes)
    - INFO: Routine operations (like "engine started")
    - WARNING: Something unusual but handled (like "tire pressure low")
    - ERROR: Something failed but system continues (like "radio malfunction")
    - CRITICAL: System- level failure ("engine failure")

    WHy does this matter?
    Because you want different information in different situations:
    - Development: See everything (DEBUG level)
    - Production: Only problems (WARNING+ level)
    - Incident investigation: Everything again (DEBUG level)

    You control this WITHOUT Changing code, just configuration.
    
    """


def demonstrate_log_levels():
    """ 
    Shows each log level and when to use it.

    This is about THINKING: "What severity is this event?"
    """
    print("\n--- LOG LEVELS EXPLAINED ---")

    # Reset logging to clear previous config
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)-8s: %(message)s',
        force=True  # Override previous configuration
    )


    logger = logging.getLogger('demo')

    print("\nDEBUG level - Detailed diagnostic information")
    logger.debug("User session initialized with token: abc123")
    logger.debug("Cache hit rate: 85%")
    logger.debug("SQL Query executed in 0.05s")
    print("-> Use for: Technical details useful when diagnosing issues")
    print("-> Who cares: Developers debugging" )
    print()

    print("INFO level - Confirmation things are working as expected")
    logger.info("User 'jhon@example.com' logged in")
    logger.info("Report generated: monthly_sales.pdf")
    logger.info("Background job completed: database backup")
    print("-> Use for: Normal operation milestones")
    print("-> Who cares: Operators, auditors, developers")
    print()

    print("WARNING level - Something unexpected but handled")
    logger.warning("API rate limit approaching (80% used)")
    logger.warning("Retrying failed network request (attempt 2/3)")
    logger.warning("Using default confuguration, no config file found")
    print("-> Use for: Degraded operation, minor issues, things to watch")
    print("-> Who cares: Operators, system administrators")


    print("ERROR level - Something failed, but system continues")
    logger.error("Failed to send email notification to user 123")
    logger.error("Payment processing failed: insufficient funds")
    logger.error("Unable to load user preference file")
    print("-> Use for: Operations that failed but didn't crash the system")
    print("-> Who cares: On-call engineers, support team")
    print()


    print("CRITICAL level - System-level failure")
    logger.critical("Database connection pool exhausted")
    logger.critical("Out of memort - unable to allocate buffer")
    logger.critical("Security: Repeated authentication failures detected")
    print("-> Use for: Emergencies, system about to fail or failed")
    print("-> Who cares: Everyone - wake people up")


def demonstrate_appropiate_levels():
    """
    Real-world example: user registration flow.

    Shows how to think about severity in context.
    """
    print("\n--- CHOOSING APPROPIATE LOG LEVELS ---")

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(message)s',
        force=True
    )


    logger = logging.getLogger('registration')

    def register_user(username, email, age):
        """
        User registration with appropiate logging at each step.
        """

        logger.info(f"Registration attempt for username: {username}")


        # Validation
        if not email or '@' not in email:
            logger.error(f"Registration failed: invalid email '{email}'")
            return False
        
        if age < 13:
            logger.warning(f"Registration blocked: age {age} below minimum")
            return False
        
        # Simulate: Chek if username taken
        logger.debug(f"Checking username availability: {username}")

        # Simulate: create user in database
        logger.debug(f"Inserting user record: {username}, {email}")

        # Sucess
        logger.info(f"User registered sucessfully: {username}")
        return True
    
    # Test cases
    test_users = [
        ('alice', 'alice@example.com', 25), # Sucess
        ('bob', 'invalid-email', 30),   # Error
        ('charlie', 'charlie@example.com', 10), # Warning
    ]

    for username, email, age in test_users:
        print(f"\n--- Attempting to register {username} ---")
        register_user(username, email, age)



# Part 4: Logging Configuration


"""
Configuration is how you control logging behavior WITHOUT changing code.

key decisions:
1. What level to show? (DEBUG in dev, WARNING in prod)
2. Where to send logs? (Console, file, remote service)
3. What format? (include timestamps, source file, etc.)

This is powerful:same code, different behavior based on environment.

"""

def demonstrate_logging_to_file():
    """
    Shoes how to log to a file instead of console.

    In real systems, logs fo to files so you can:
    - Review them later
    - Parse them with tools
    - Keep them even after program ends
    - Rotate them (keep last N days)
    
    """

    print("\n--- LOGGING TO FILE ---")

    # Create a log file
    log_filename = 'application.log'

    # Configure logging to write to file
    logging.basicConfig(
        level=logging.INFO, # Only INFO and above
        format='%(asctime)s [%(levelname)s] %(name)s %(message)s',
        filename=log_filename,   # Logs go to file, not console
        filemode='w',   # 'W' = overwrite, 'a' = append
        force=True
    )


    logger = logging.getLogger('file_demo')

    logger.info("Application started")
    logger.debug("This DEBUG won't appear (level is INFo)")
    logger.warning("Configuration file not found, using deafaults")
    logger.info("Application shutdown")

    print(f"\nLogs written to {log_filename}")
    print("File contents:")
    print("-" * 60)
    with open(log_filename, 'r') as f:
        print(f.read())
    print("-" * 60)


def demonstrate_dual_logging():
    """
    Shows logging to BOTH console AND file simultaneously.

    This is common in real systems:
    - Console: For immediate feedbacks
    - File: For persistence and analysis

    Uses handlers to route logs to multiple destinations
    
    """


    print("\n-- DUAL LOGGING: Console + File ---")


    # Create logger
    logger = logging.getLogger('dual_logger')
    logger.setLevel(logging.DEBUG)


    # Remove existing handlers (clean slate)
    logger.handlers.clear()

    # Handler 1: Console (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # Only INFO+ to console
    console_format = logging.Formatter('%(levelname)s: %(message)s')
    console_handler.setFormatter(console_format)
    logger.addHandler(console_handler)


    # Handler 2: File
    file_handler = logging.FileHandler('detailed.log', mode='w')
    file_handler.setLevel(logging.DEBUG)    # Everything to file
    file_format = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )  
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)


    # Now log some messages
    logger.debug("Detailed debug info (only in file)")
    logger.info("Important information (console AND file)")
    logger.warning("Warning message (console AND file)")
    logger.error("Error occured (console AND file)")

    print("\n Logs sent to both console (above) and detailed.log")
    print("\ndetailed.log contents:")
    print("-" * 60)
    with open('detailed.log', 'r') as f:
        print(f.read())
    print("-" * 60)





# Part 5: Logging exceptions properly

"""
One of logging's most powerful features: capturing full exception details


When an exception occurs, you want to log:
- The error message
- The exception type
- The full traceback (stack trace)

logger.exception() does this automatically.

"""


def demonstrate_exception_logging():
    """
    Shows the right way to log exceptions.

    This is critical for debugging production issues.

    """
    print("\n--- LOGGING EXCEPTIONS---")


    logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s [%(levelname)s %(message)s]',
        force=True
    )

    logger = logging.getLogger('exception_demo')

    def risky_operation(data):
        """
        Operation that might fail in various ways.
        """
        try:
            # Multiple failure points
            result = int(data['value']) / data['divisor']
            return result
        
        except KeyError as e:
            # Log with full exception details
            logger.exception("Missing required field in data")
            #This logs the error message AND the full stack trace
            return None
        
        except (ValueError, TypeError) as e:
            logger.exception(f"Data type error: {e}")
            return None
        
        except ZeroDivisionError as e:
            logger.exception("Division by zero attempted")
            return None
        
    
    # Test cases that trigger the different exceptions
    test_cases = [
        {'value': '10', 'divisor': 2}, # Sucess
        {'value': '10'},                # KeyError
        {'value': 'abc', 'divisor': 2},  # ValueError
        {'value': '10', 'divisor': 0}, # ZeroDivisionError

    ]

    for i, data in enumerate(test_cases, 1):
        print(f"\n--- Test case {i}: {data} ---")
        result = risky_operation(data)
        if result:
            print(f"Result: {result}")
        else:
            print(" Operation failed (check logs for details)")



def demonstrate_logging_best_practices():
    """
    Brings together all concepts into realistic example

    Shows how logging makes code observable and debuggable.
    """

    print("\n--- COMPLETE EXAMPLE: Best Practices ---")

    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(funcName)s: %(message)s',
        force=True
    )

    logger = logging.getLogger('best_practices')

    def process_user_data(user_id, data):
        """
        Complete function with appropiate logging throughout.

        Notice:
        - DEBUG: Technical details
        - INFO: Normal Operations
        - WARNING: Handled issues
        - ERROR: Failures
        - exception(): Logging with ful traceback
        
        """

        logger.info(f"Processing data for user {user_id}")
        logger.debug(f"Input data: {data}")


        try:
            # Validation
            if not isinstance(data, dict):
                logger.error(f"Invalid data type: expected dict, got {type(data)}")
                return False
            
            required_fields = ['name', 'email']
            missing = [f for f in required_fields if f not in data]
            if missing:
                logger.warning(f"Missing optional fields: {missing}")

            # Processing
            logger.debug(f"Validating email: {data.get('email')}")

            if '@' not in data.get('email', ''):
                logger.error(f"Invalid email format: {data.get('email')}")
                return False
            
            # Simulate database operation
            logger.debug(f"Saving to database: user {user_id}")

            # Sucess
            logger.info(f"User {user_id} processed successfully")
            return True
        
        except Exception as e:
            # Unexpected error - log with full traceback
            logger.exception(f"Unexpected error processing user {user_id}")
            return False
        

        # Test the function
        test_cases = [
            (1, {'name': 'Alice', 'email': 'alice@example.com'}),
            (2, {'name': 'Bob'}), # Missing email
            (3, "not a dict"),  # Wrong type

        ]


        for user_id, data in test_cases:
            print(f"\n--- Processing user {user_id} ---")
            sucess = process_user_data(user_id, data)
            print(f"Result: {'Sucess' if sucess else 'x Failed'}")




# PArt 6: When to use logging vs print


"""
Decision guide:

Use print() when:
- direct user interaction (CLI tools, prompts)
- quick debugging during development
- teaching/demonstrating code
- program's actual output (not side effects)

Use logging when:
- recording progra behavior for later review
- anything in production
- long-running processes
- library code (user control logging, not output)
- anything you might need to debug later
- severity matters
- multiple destinations needed

"""

def demonstrate_print_vs_logging():
    """
    Side-by-side comparison showing when to use each.
    """
    print("\n--- PRINT VS LOGGING: When to Use Each ---")

    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s',
        force=True
    )

    logger = logging.getLogger('comparison')

    print("\n=== CLI Tool Example ===")
    # Print for user interaction
    user_name = "Alice"
    print(f"Welcome, {user_name}!") # Direct user communication
    print("Select an option:")
    print("1. View profile")
    print("2. Edit settings")


    # Logging fot what the program does
    logger.info(f"User {user_name} started session")
    logger.debug(f"Loading uset preferences for {user_name}")

    print("\n=== Background Process Example ===")
    # No print() here - it's a background process, no user watching
    logger.info("Background job started: email digest")
    logger.debug("Loading user preferences")
    logger.info("Emails sent: 150")
    logger.info("background job completed")


    print("\nGuideline:")
    print("- print() = talking To the user")
    print("- logging = talking ABOUT the program")


# MAIN DEMONSTRATION


if __name__ == "__main__":
    print("=" * 70)
    print("LOGGING AS A SYSTEM SKILL")
    print("=" * 70)

    # Demo 1: Why print() isn't enough 
    demonstrate_print_limitation()

    # Demo 2: Basic Logging
    demonstrate_basic_logging()

    # Demo 3: Log levels
    demonstrate_log_levels()
    demonstrate_appropiate_levels()

    # Demo 4: Configuration
    demonstrate_logging_to_file()
    demonstrate_dual_logging()

    # Demo 5: Exception logging
    demonstrate_exception_logging()
    demonstrate_logging_best_practices()

    # Demo 6: Print vs Logging
    demonstrate_print_vs_logging()


    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("""
    1. Logging creates a persistent record of program bahavior
    2. print() is for users; Logging is for developers/operators
    3. Log levels categorize severity: DEBUG, INFO, WARNING, ERROR, CRITICAL
    4. Configure logging for different environments without code changes
    5. Use logger.exception() to capture full error details
    6. Good logging makes your code observable and debuggable
          


    MENTAL MODEL:
          Imagine your program running on a server at 3 AM when something breaks.
          Your logs are the ONLY way yo know what happened.
          Log as if future-you is debugging in the dark.

          PRACTICAL RULE:
          - Development: level=DEBUG (see everything)
          - Production: level=WARNING (only problems)
          - Incident investigation: level=DEBUG (see everything again)      
          """)

    # Cleanup
    import os
    for file in ['application.log', 'detailed.log']:
        try:
            os.remove(file)
        except:
            pass


        










    