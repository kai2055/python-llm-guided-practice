
# ===========================================================
# CLASS HIEARCHY IN PYTHON
# Topic: Object-Oriented Programming (OOP) - Inheritance and Class Hierarchy
# Context: ML Data Validation (Simple, beginner-friendly)
# ============================================================


# PART 1: THE BASE (PARENT) CLASS



# What is a class?
# A class is a blueprint for creating objects. Think of it like a cookie cutter -
# the class defines the shape, and objects are the actual cookies you make.


# What is a parent/base class?
# A parent class contains common features that multiple child classes will share.
# Instead of writing the same code multiple times, we write it once in the parent.

class DataValidator:
    """
    This is our PARENT (or BASE) class.

    Purpose: Define common validation behavior that ALL validators  should have.

    Syntax breakdown:
    - 'class' keyword tells Python we are defining a class
    - 'DataValidator' is the class name (use CamelCase by convention)
    - The colon ':' starts the class definition block
    - Triple quotes create a docstring (documentation for the class)
    
    """

    # The __init__ method is the CONSTRUCTOR
    # It runs automatically when you create a new object from this class
    # It's where you set up the initial state of your object


    def __init__(self, field_name):
        """
        Constructor method - initializes a new DataValidator object.

        Parameters:
        - self: refers to the object being created (like 'this' in other languages)
        - field_name: the name of the data field we are validating (e.g "age), email)

        Syntax note:
        - 'self' MUST be the first parameter in all class methods
        - When you call the method, Python passes 'self' automatically
         
        """

        # Instance variables (also called attributes)
        # These belong to each individual  object created from the class
        # The 'self.' prefix means "this specific object's variable"

        self.field_name = field_name  # Store which field this validator checks
        self.error_count = 0          # Track how many validation errors we have found
        self.errors = []              # Store specific error messages

        # Why use self?
        # So each validator object can have its own field_name, error_count, etc.
        # If we created 10 validators, each would have independent values.


    
    # Regular methods (functions inside a class)
    # Thes define what objects of this class can DO

    def validate(self, value):
        """
        The main validation method.

        This is a GENERIC method in the parent class.
        Child classes will OVERRIDE this to provide specific validation logic


        For now, it just passes (does nothing) - this  is intentional!
        We expect child classes to replace this with their own logic.

        """
        # 'pass' means "do nothing" - it's a placeholder
        # We define this method here so all validators have it,
        # but each child class will implement it differently 
        pass


    def record_error(self, value, reason):
        """
        Record when validation fails.

        This method is SHARED by all child classes.
        Any child can call this method to log errors in the same way.

        Parameters:
        - value: the data that failed validation
        - reason: why it failed
        
        """
        self.error_count += 1   # Increment the counter
        

        # Create a formatted error message
        error_message = f"Field '{self.field_name}': value '{value}' failed - {reason}"

        # Add to our error list
        self.errors.append(error_message)

        # f-strings (f".....") let you embed variables directly in strings
        # The curly braces {} get replaced with variable values



    def get_report(self):
        """
        Generate a summary report of validation results.


        This is another SHARED method - all validators can use it.
        """
        if self.error_count == 0:
            return f"Field '{self.field_name}': All validations passed!"
        else:
            # Join all error messages with newlines
            report = f"x Field '{self.field_name}': {self.error_count} errors found:\n"
            report += "\n".join(self.errors)
            return report
        



# PART 2: CHILD CLASSES (INHERITANCE)



# What is inheritance?
# A child class INHERITS everything from its parent class.
# It gets all the parent's methods and attributes automatically.
# Then it can ADD new features or MODIFY existing ones.


class NumericValidator(DataValidator):
    """
    This is a CHILD class that inherits from DataValidator.

    Syntax: class ChildName(ParentName):
    - Putting 'DataValidator' in parentheses means this class inherits from it
    - NumericValidator automatically gets all DataValidator's methods

    Purpose: Validate numeric data (integers, floats) with range checking

    """

    def __init__(self, field_name, min_value=None, max_value=None):
        """
        Constructor for NumericValidator

        Notice we are EXTENDING the parent's constructor:
        - Parent needed: field_name
        - We ADD: min_value and max_value (specific to numeric validation)

        Parameters have default values (None) - they are optional
    
        """

        # SUPER() - This is crucial for inheritance!
        # super() lets us call the parent class's methods
        # Here, we call the parent's __init__ to set up field_name, error_count, errors
        super().__init__(field_name)

        # Why use super()?
        # So we don't duplicate code. The parent already knows  how to initialize
        # filed_name and error tracking - we reuse that logic

        # Now add our child-specific attributes
        self.min_value = min_value  # Minimum acceptable value (or None if no minimum)
        self.max_value = max_value  # Maximum acceptable value (or None if no maximum)


    def validate(self, value):
        """
        OVERRIDE the parent's validate method with numeric-specific logic.

        Method overriding: defining a method in child that has the same name as parent
        When you call .validate() on a NumericValidator object, THIS version runs,
        not the parent's pass statement.
        
        """

        # Check 1: Is the value actually a number?
        if not isinstance(value, (int, float)):
            # isinstance() checks if value is of specified type(s)
            # (int, float) is a tuple of acceptable types
            self.record_error(value, f"Exepected a number, for {type(value).__name__}")
            return False
        
        # Check 2: Is it within the minimum bound?
        if self.min_value is not None and value < self.min_value:
            # 'is not None' checks if min_value was actually set
            self.record_error(value, f"Below minimum ({self.min_value})")
            return False
        
        # Check 3: Is it within maximum bound?
        if self.max_value is not None and value > self.max_value:
            self.record_error(value, f"Above maximum ({self.max_value})")
            return False
        
        # If all checks pass, return True
        return True
    


class TextValidator(DataValidator):
    """
    Another CHILD class - validates text/string data.

    This demonstrates that multiple classes inherit from the same parent.
    Each child specializes the parent's generic functionality differently.
    """

    def __init__(self, field_name, min_length=None, max_length=None, allowed_chars=None):
        """
        Constructor with text-specific parameters.

        Again, we call super().__init__() to handle the parent's initialization.

        """
        super().__init__(field_name)

        # Child-specific attributes for text validation
        self.min_length = min_length    # Minimum string length
        self.max_length = max_length    # Maximum string length
        self.allowed_chars = allowed_chars  # Set of allowed characters (or None)

    
    def validate(self, value):
        """
        OVERRIDE validate() with text-specific checks.

        Notice: same method name as NumericValidator.validate, but different logic!
        This is POLYMORPHISM - different classes responding to the same method call
        in their own way
        """

        # Check 1: Is it a string?
        if not isinstance(value, str):
            self.record_error(value, f"Expected text, got {type(value).__name__}")
            return False
        
        # Check 2: Minimum length
        if self.min_length is not None and len(value) < self.min_length:
            # len() returns length of string
            self.record_error(value, f"Too short (min: {self.min_length} characters.)")
            return False
        
        # Check 3: Maximum length
        if self.max_length is not None and len(value) > self.max_length:
            self.record_error(value, f"Too long (max: {self.max_length} characters)")
            return False
        
        # Check 4: Character restrictions
        if self.allowed_chars is not None:
            # Check is all characters in value are in allowed_chars
            for char in value:
                if char not in self.allowed_chars:
                    self.record_error(value, f"Contains invalid character: {char}")
                    return False
                
        return True
    


class EmailValidator(TextValidator):
    """
    A GRANDCHILD class - inherits from TextValidator, which inherits from DataValidator

    This demonstrates MULTI-LEVEL INHERITANCE:
    EmailValidator -> TextValidator -> DataValidator

    EmailValidator gets features from BOTH parents:
    - From DataValidator: field_name, error_count, record_error, get_report
    - From TextValidator: min_length, max_length, text validation logic

    """

    def __init__(self, field_name):
        """
        Email-specific constructor.

        We set reasonable defaults for email validation by calling
        the parent TextValidator's __init__ with specific values
        
        """

        # Call TextValidator's constructor with email-appropiate constraints
        # min_length=5 because shortes email is like "a@b.c"
        # max_length=1oo is a reasonable email length limit
        super().__init__(field_name, min_length=5, max_length=100)

    def validate(self, value):
        """
        OVERRIDE validate() again with email-specific logic.

        Here we do something interesting: we call the PARENT's validate method
        first (using super()), then add additional email-specific checks.

        """

        # First, use parent's text validation (length checks, etc.)
        # If basic text validation fails, no point checking email for format
        if not super().validate(value):
            return False
        
        # Now add email-specific validation
        # Check for @ symbol
        if '@' not in value:
            self.record_error(value, "Missing '@' symbol")
            return False
        
        # Check for domain (something after @)
        parts = value.split('@')
        # split() divides string at @ into a list

        if len(parts) != 2:
            # Should be exactly 2 parts: local@domain
            self.record_error(value, "Invalid email format (multiple @ symbols)")
            return False
        
        local_part, domain_part = parts
        # Unpacking: assign first element to local_part, second to domain_part

        if len(local_part)== 0:
            self.record_error(value, "Missing local part before @")
            return False
        
        if len(domain_part) == 0:
            # Domain should have at least one dot (e.g, gmail.com)
            self.record_error(value, "Domain missing extension (like .com)")
            return False
        
        return True
    



# PART 3: USING THE CLASS HIERARCHY (DEMONSTRATION)



def demonstrate_class_hierarchy():
    """
    This function demonstrates how our class hierarchy works.

    We will create objects from each class and see inheritance in action

    """

    print("=" * 80)
    print("DEMONSTRATION CLASS HIERARCHY IN PYTHON")
    print("=" * 80)
    print()




    # Example 1: NumericValidator
    print("--- Example 1: Validating Age (Numeric Data)----")
    print()

    # Create a NumericValidator object
    # This calls NumericValidator.__init__()
    age_validator = NumericValidator(field_name="age", min_value=0, max_value=120)

    # What just happened ?
    # 1. Python created a new object
    # 2. Called NumericValidator.__init__(age_validator, "age", 0, 120)
    # 3. Inside __init__, super().__init__("age") called DataValidator's constructor
    # 4. Now age_validator has ALL attributes from both classes


    # Test with various ages
    test_ages = [25, -5, 150, "thirty", 45.5]

    for age in test_ages:
        result = age_validator.validate(age)
        # This calls NumericValidator.validate(), NOT DataValidator.validate()
        # Even though age_validator "is a" DataValidator, it's specifically a NumericValidator
        status = "Valid" if result else "Invalid"
        print(f" Testing age={age}: {status}")

    print()
    print(age_validator.get_report())
    # get_report() is inherited from DataValidator - we didn't rewrite it!
    print()
    print()


    # Example 2: TextValidator

    print("--- Example 2: Validating Username (Text Data) ---")
    print()


    # Create TextValidator with specific rules
    username_validator = TextValidator(
        field_name="username",
        min_length=3,
        max_length=20,
        allowed_chars=set("abcdefghijklmnopqrstuvwxyz0123456789_")
        # set() creates a collection of unique characters

    )

    test_usernames = ["alice", "ab", "this_username_is_way_too_long_for_Our_system", "user@1234", "bob_42"]

    for username in test_usernames:
        result = username_validator.validate(username)
        status = "valid" if result else "invalid"
        print(f"Testing username='{username}': {status}")


    print()
    print(username_validator.get_report())
    print()
    print()


    # Example 3: EmailValidator

    print("--- Example 3: Validating Email (Multi-level Inheritance)")
    print()


    emial_validator = EmailValidator(field_name="email")

    # Notice: EmailValidator didn't need min_length/max_length parameters
    # because its __init__ sets sensible defaults

    test_emails = [
        "username@example.con"      # Valid
        "invalid.email"             # Missing @
        "@example.com"              # Missing local parts
        "user@"                     # Missing domain
        "user@domain"               # Missing dot in domain
        "a@b.co"                    # Valid (minimal)
    ]


    for email in test_emails:
        result = emial_validator.validate(email)
        status = "valid" if result else "invalid"
        print(f"Testing email='{email}': {status}")


    print()
    print()
    print(emial_validator.get_report())
    print()



    # Example 4: Polymorphism

    print("--- Example 4: Polymorphism in Action ----")
    print()
    print("Polymorphism means: different objects respond to the same method")
    print("in their own way. Watch how validate() behaves differently: ")
    print()

    # Create a list of different validator types
    # They are all DataValidators (via inheritance), but each validates differetly

    validators = [
        NumericValidator("score", min_value=0, max_value=100),
        TextValidator("name", min_length=2, max_length=50),
        EmailValidator("contact_email")
    ]

    # Test the same value on all validators
    test_value = "hello@world"

    for validator in validators:
        # Same method call (.validate), but different behavior based on object type!
        result = validator.validate(test_value)
        print(f" {validator.__class__.__name__}: {result}")
        # __class__.__name__ gives us the class name as a string


    print()
    print("Why different results?")
    print("- NumericValidatoe checks if it's a number")
    print("- TextValidator checks string length/characters")
    print("- EmailValidator checks email format")
    print("Same method name, different implementations!")
    print()



    # Key Concepts Summary

    print("=" * 80)
    print("KEY CONCEPTS DEMONSTRATED:")
    print("=" * 80)
    print("""
1. CLASS HIERARCHY:
            - Parent class (DataValidator) defines common functionality
            - Child classes (NumericValidator, TextValidator) inherit and specialize
            - Grandchild class (EmailValidator) inherits from child
          
2. INHERITANCE:
            - Child classes automatically get parent's methods and attributes
            - Use super() to call parent's methods
            - Reduces code duplication

3. METHOD OVERRIDING:
          - Child classes can replace parent's methods with their own version
          - NumericValidator.validate() replaces DataValidator.validate()

4. POLYMORPHISM:
          - Different objects respond to the same method call differently
          - All validators have .validate(), but each implements it uniquely

5. CODE REUSE:
          - record_error() and get_report() defined once, used by all
          - Don't Repeat Yourself (DRY) priniciple

6. SPECIALIZATION:
          - Each child adds specific attributes (min_value, max_value, etc.)
          - Each child implements validation logic appropriate to its data type  

""")
    

# PART 4: RUN THE DEMONSTRATION

# This is the standard Python idiom for "run this code only when the script
# is executed directly, not when it's imported as a module"
if __name__ == "__main__":
    demonstrate_class_hierarchy()

    
