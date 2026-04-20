

"""
MODULE: Exception Handling Practice And Control Flow
DATE: 2026-04-20

"""

# Fix the following code:
# try:
#     result = int("abc")
# except ValueError, TypeError:
#     print("conversion failed")
# finally:
#     print("done")


# Answer

try:
    result = int("abc")
except (ValueError, TypeError):
    print("conversion failed")
finally:
    print("done")




# Fill in the blanks

"""
def classify(score):
    if ___:           # 90 and above
        return "A"
    ___ score >= 70:
        return "B"
    elif ___:         # 50 to 69
        return "C"
    ___:
        return "F"

classify(95)  # → "A"
classify(45)  # → "F"


"""



def classify(score):
  if score >= 90:
    return "A"
  elif score >= 70:
    return "B"
  elif score >= 50:
    return "c"
  else:
    return "f"


print(f"{classify(45)}")



"""
for i in range(10):
    if i % 2 == 0:
        continue
    if i > 9:
        break
    print(i)
# Expected: 1 3 5 7 9


"""


for i in range(10):
  if i % 2 != 0:
    print(i)



"""
	safe_get
Write a function that safely retrieves a value from a dict. If key is missing return default. If value is not expected_type raise TypeError with clear message.
data = {"score":88,"name":"Anna"}
safe_get(data, "score", expected_type=int)     # → 88
safe_get(data, "missing", default=0)           # → 0
safe_get(data, "name", expected_type=int)      # raises TypeError: ...

"""

data = {"score": 88, "name": "Anna"}

def safe_get(my_dict, k, default=None, expected_type=None):
   
   if k not in my_dict:
      return default
   
   value = my_dict[k]

   if expected_type is not None and not isinstance(value, expected_type):
      raise TypeError(f"The value is not of type {expected_type.__name__}")
   
   return value

print(safe_get(data, "score", expected_type=int))     # 88
print(safe_get(data, "missing", default=0))           # 0
# print(safe_get(data, "name", expected_type=int)) 



"""
parse_int_safe

Write a function that tries to convert a value to int. If it fails return a default. Never raise an exception to the caller.
parse_int_safe("42")         # → 42
parse_int_safe("abc")        # → None
parse_int_safe("abc", -1)    # → -1
parse_int_safe(3.9)          # → 3

"""
def parse_int_safe(num, default=None):
  try:
    changed = int(num)
  except:
    return default
  else:
    return changed



print(f'{parse_int_safe("42")}')
print(parse_int_safe("42"))      # 42
print(parse_int_safe("abc"))     # None
print(parse_int_safe("abc", -1)) # -1
print(parse_int_safe(3.9))       # 3


"""
retry with backoff
Write retry(func, times, delay) that retries a function up to "times" times. Wait "delay" seconds between attempts (use time.sleep). If all attempts fail, raise the last exception. Print each failed attempt with the attempt number.
import random, time
def flaky():
    if random.random() < 0.7: raise ConnectionError("timeout")
    return "ok"

retry(flaky, times=5, delay=0.5)
# prints: "Attempt 1 failed: timeout"
# prints: "Attempt 2 failed: timeout"
# returns "ok" or raises ConnectionError after 5 tries


"""


import random, time

def flaky():
   if random.random() < 0.7:
      raise ConnectionError("Timeout")
   
   return "ok"



def retry(flaky, times, delay):
    for i in range(times):          
        try:
            result = flaky()
            return result
        except ConnectionError as e:
            print(f"Attempt {i + 1} failed")
            time.sleep(delay)
    raise ConnectionError("All attempts failed")  


print("Test 3:")
result = retry(flaky, times=3, delay=0.1)
print(f"Result: {result}\n")      
