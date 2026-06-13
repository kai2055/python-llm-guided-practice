"""
COMPLETE GUIDE: GETTERS, SETTERS, AND @property DECORATOR
Understanding how to control attribute access in Python.
"""

class MLConfig:
    """
    Demonstrates getters, setters, and the @property decorator
    """

    def __init__(self, learning_rate):
        # This calls the setter method (because we use self.learning_rate)
        self.learning_rate = learning_rate

    # =============== GETTER =====================
    @property
    def learning_rate(self):
        """
        GETTER - What is a getter?
        A getter is a method that RETURNS a value when someone tries to READ an attribute.

        When you write:     value = config.learning_rate
        Python calls:       value = config.learning_rate()  (this getter method)

        Purpose:
        - Retrieve the value of a private attribute
        - Can add logic when reading (logging, calculations, etc.)
        - Controls what users see when they access the attribute
        """
        print("   [GETTER is running] Retrieving _learning_rate value")

        # You could add logic here, like:
        # - Log every time someone reads this value
        # - Return a default value if none exists
        # - Calculate the value on the fly
        # - Return a transformed version of the data

        return self._learning_rate   # Return the private stored value
    
    # ============== SETTER =============
    @learning_rate.setter
    def learning_rate(self, value):
        """
        SETTER - What is a setter?
        A setter is a method that runs when someone tries to ASSIGN a value to an attribute.

        When you write:     config.learning_rate = 0.5
        Python calls:       config.learning_rate(0.5)  (this setter method)

        Purpose:
        - VALIDATE data before storing it (most common use)
        - Transform data before storing (convert types, normalize, etc.)
        - Prevent invalid or dangerous assignments
        - Trigger side effects when value changes (notifications, updates)
        """
        print(f"   [SETTER is running] Checking value: {value}")

        # VALIDATION LOGIC - The main reason for setters
        if not (0.0 < value <= 1.0):
            # Raise error to prevent invalid value from being stored
            raise ValueError(f"Invalid learning rate {value}: Must be between 0.0 (exclusive) and 1.0 (inclusive)")
        
        # TRANSFORMATION (optional)
        # You could modify the value before storing
        # value = round(value, 3)  

        print(f"   [SETTER] Validation passed! Storing {value}")

        # Store in PRIVATE variable (underscore convention)
        # IMPORTANT: Store in self._learning_rate NOT self.learning_rate
        # Because self.learning_rate = value would call this setter again!
        self._learning_rate = value

    # =========== WITHOUT PROPERTY (Traditional Way) ============
    # This shows what @property replaces - for comparison only

    def get_learning_rate_traditional(self):
        """Traditional getter method (without @property)"""
        return self._learning_rate
    
    def set_learning_rate_traditional(self, value):
        """Traditional setter method (without @property)"""
        if not (0.0 < value <= 1.0):
            raise ValueError("Learning rate must be between 0.0 and 1.0")
        self._learning_rate = value


# ============== DEMONSTRATION ==============

print("=" * 70)
print("Understanding GETTERS and SETTERS")
print("=" * 70)

# Create object
print("\n1. CREATING OBJECT: config = MLConfig(0.01)")
print("   ↓ This triggers the SETTER during initialization")
config = MLConfig(0.01)
print("   ✓ Object created")

# READING (triggers GETTER)
print("\n2. READING VALUE: result = config.learning_rate")
print("   ↓ This triggers the GETTER")
result = config.learning_rate
print(f"   Result received: {result}")

# WRITING (triggers SETTER)
print("\n3. WRITING VALUE: config.learning_rate = 0.75")
print("   ↓ This triggers the SETTER")
config.learning_rate = 0.75
print(f"   New value: {config.learning_rate}")

# WHY WE NEED GETTERS AND SETTERS:
print("\n" + "=" * 70)
print("WHY GETTERS AND SETTERS ARE IMPORTANT")
print("=" * 70)

class WithoutValidation:
    """Class with NO getter/setter - direct attribute access"""
    def __init__(self, rate):
        self.learning_rate = rate  # Direct access, no control

print("\nPROBLEM 1: Without setters, NO VALIDATION possible:")
bad_config = WithoutValidation(999)
print(f"   Bad value allowed: learning_rate = {bad_config.learning_rate}")

bad_config.learning_rate = -5
print(f"   Even negative works: learning_rate = {bad_config.learning_rate}")
print("   ❌ No validation! Data corruption possible!")

print("\nPROBLEM 2: Without getters, NO CONTROL over what's returned:")
class NoGetterControl:
    def __init__(self):
        self._secret = "sensitive data"
        # No getter - anyone can access directly
        # Can't add logging, can't control access

print("\n" + "=" * 70)
print("COMPARISON: TRADITIONAL vs @property SYNTAX")
print("=" * 70)

class TraditionalWay:
    """Old Java-style: Manual getter/setter methods"""
    def __init__(self, rate):
        self.set_learning_rate(rate)

    def get_learning_rate(self):  # Manual getter
        return self._learning_rate
    
    def set_learning_rate(self, value):  # Manual setter
        if not (0.0 < value <= 1.0):
            raise ValueError("Invalid value")
        self._learning_rate = value

class PropertyWay:
    """Python-style: @property decorator"""
    def __init__(self, rate):
        self.learning_rate = rate  # Same as TraditionalWay, but cleaner

    @property
    def learning_rate(self):  # Acts like get_learning_rate()
        return self._learning_rate
    
    @learning_rate.setter
    def learning_rate(self, value):  # Acts like set_learning_rate()
        if not (0.0 < value <= 1.0):
            raise ValueError("Invalid value")
        self._learning_rate = value

print("\nTRADITIONAL WAY (ugly syntax):")
trad = TraditionalWay(0.1)
print(f"   Get: trad.get_learning_rate() = {trad.get_learning_rate()}")
trad.set_learning_rate(0.5)
print(f"   Set: trad.set_learning_rate(0.5)")
print(f"   Get again: {trad.get_learning_rate()}")
print("   ❌ Must remember method names: get_xxx(), set_xxx()")

print("\n@property WAY (beautiful syntax):")
prop = PropertyWay(0.1)
print(f"   Get: prop.learning_rate = {prop.learning_rate}")
prop.learning_rate = 0.5
print(f"   Set: prop.learning_rate = 0.5")
print(f"   Get again: {prop.learning_rate}")
print("   ✓ Clean! Looks like normal attribute access!")
print("   ✓ Validation still happens behind the scenes!")

# Additional test to show validation error
print("\n" + "=" * 70)
print("TESTING VALIDATION ERROR")
print("=" * 70)

try:
    print("\nTrying to create config with invalid value 1.5:")
    bad_config = MLConfig(1.5)
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

try:
    print("\nTrying to set invalid value 0:")
    config.learning_rate = 0
except ValueError as e:
    print(f"   ✓ Error caught: {e}")

print("\n" + "=" * 70)
print("QUICK REFERENCE")
print("=" * 70)
print("""
┌─────────────────────────────────────────────────────────────┐
│  KEY RULE:                                                  │
│  ✓ In setter: self._variable = value                       │
│  ✗ In setter: self.variable = value  (INFINITE LOOP!)      │
├─────────────────────────────────────────────────────────────┤
│  @property     → Creates getter (reading)                   │
│  @.setter      → Creates setter (writing with validation)  │
│  _variable     → Private variable (actual storage)         │
└─────────────────────────────────────────────────────────────┘
""")