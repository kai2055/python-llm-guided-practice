# Write a function that takes a value and a list of functions
# appplies them in sequence, and returns the final result


#   def double(x): return x * 2
#   def add_ten(x): return x + 10
#   def square(x): return x ** 2

#   apply_pipeline(3, [double, add_ten, square])   # → (3*2+10)^2 = 256
#   apply_pipeline(5, [])                          # → 5  (no functions = unchanged)

def double(x): return x * 2
def add_ten(x): return x + 10
def square(x): return x ** 2

def apply_pipeline(n:int,functions:list)-> int:
    """
    Function that takes a number and applies different functions
    in a sequence

    args:
        n (int): the number of functions applied

        functions   (list): list containing the functions for the pipeline

    returns:
        int: final value after all the function operations are carried out
    

    """

    if not functions:
        return n
    
    result = n

    for fun in functions:
        result = fun(result)

    return result


r = apply_pipeline(3, [double, add_ten, square])
print(r)

# Write a function that divides by b. If b is zero, return a default value.
# If a or b is not a number, raise a TypeError with a clear message


def safe_divide(num:int, divisor:int, default= 0)-> int:
    """
    Function that takes and number and a divisor and returns their quotient

    args:
        num (int): The number to be divided
        divisor (int): The divisor of the number

    returns:
        int: The quotient of the division

    Raises:
        TypeError: if the divisor or num is not a number
    
    """

    if divisor == 0:
        return default
    
    if not isinstance(num,(int, float)) or not isinstance(divisor,(int, float)):
        raise TypeError("Either the number or the divisor is not an int")
    
    return num / divisor



r = safe_divide(10,"2")
print(r)




