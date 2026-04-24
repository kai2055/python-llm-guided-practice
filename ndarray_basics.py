
import numpy as np


print("1. Creating ndarrays")
print("=" * 60)



a = np.array([1, 2, 3, 4, 5])           # 1D array (a "vector")
b = np.array([[1, 2, 3], [4, 5, 6]])    # 2D array (a "matrix")

print(f"a = {a}")
print(f"b = \n{b}")
print(f"type(a) = {type(a)}")       # numpy.ndarray


# Attributes 

# shape -> tuple describing the size along each axis
# dtype -> the single data type of every element
# ndim -> number of dimensions (len of shape)


print("\n" + "=" * 60)
print("2. Inspecting arrays")
print("=" * 60)


print(f"a.shape = {a.shape}")           # (5,)      -> 1D, 5 elements
print(f"b.shape = {b.shape}")           # (2, 3)    -> 2 rows, 3 cols
print(f"b.dtype = {b.dtype}")           # int64 (platform-dependent)
print(f"b.ndim = {b.ndim}")             # 2



print("\n" + "=" * 60)
print("3. Common ways to create arrays")
print("=" * 60)

zeroes = np.zeros((2,3))            # all zeroes, shape (2, 3)
ones = np.ones((2,3))               # all ones
rng_arr = np.arange(0, 10, 2)      # [0 2 4 6 8 ] - like range()
linsp = np.linspace(1, 1, 5)       # 5 evenly spaces between 0 and 1


# Modern Numpy RNG API - this is the one you will see in real code
# The older np.random.rand / np.random.randn still work but are
# considered legacy. Build the habit of using default_rng from day one.

rng = np.random.default_rng(seed=42)
rand = rng.standard_normal(size=(2, 3)) # normal distribution, mean 0, std 1

print(f"zeros = \n{zeroes}")
print(f"arange = {rng_arr}")
print(f"linespace = {linsp}")
print(f"random = \n{rand}")


# 4. Indexing and slicing
# Works like Python lists but extends to multiple dimensions
# The convention is arr[rows, cols] for 2D

print("\n" + "=" * 60)
print("4. Indexing")
print("=" * 60)


m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(f"m[0, 0] = {m[0, 0]}")       # 10 - top-left
print(f"m[1, :] = {m[1, :]}")        # [40, 50, 60] - whole row 1
print(f"m[:, 2] = {m[:, 2]}")          # [30, 60, 90] - whole col 2
print(f"m[0:2, 1:] = \n{m[0:2, 1:]}")    # top-right 2 x 2 submatrix



# Vectorized operations


print("=" * 60)
print("5. Vectorized math")
print("=" * 60)

x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30, 40])

print(f"x + y = {x + y}")       # [11 22 33 44]
print(f"x * 2 = {x * y}")       # [2 4 6 8]
print(f"x ** 2 = {x ** 2}")     # [1 4 9 16]
print(f"x @ y = {x @ y}")       # 300 - dot product



# Aggregations (scalar version - axis comes later)

# Aggregations collapse an array down to fewer values.
# Without an 'axis' argument, they collapse ALL values to a single scalar.
# There is also an 'axis' argument for collapsing along one dimension


print("\n" + "=" * 60)
print("6. Scalar aggregations")
print("=" * 60)


data = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(f"data.sum() = {data.sum()}")     # 21 - grand total
print(f"data.mean() = {data.mean()}")   # 3.5 grand mean
print(f"data.std() = {data.std():.4f}")
print(f"data.min() = {data.min()}")
print(f"data.max() = {data.max()}")


# 7. Reshaping (critical for ML - wrong shapes crash everything)

print("\n" + "=" * 60)
print("7. Reshape")
print("=" * 60)

flat = np.arange(12)        # [0 1 2 ..... 11]
reshaped = flat.reshape(3, 4)   # 3 rows, 4 cols
auto = flat.reshape(2, -1)      # -1 means "figure it out"

print(f"flat.shape = {flat.shape}")
print(f"reshaped = \n{reshaped}")
print(f"auto (2, -1) = \n{auto}")       # becomes (2, 6)




# 8. Boolean masking 

print("\n" + "=" * 60)
print("8. Boolean masking")
print("=" * 60)


v = np.array([3, 1, 4, 5, 9, 2, 6])
mask = v > 3            # array of True/False

print(f"mask           = {mask}")
print(f"v[mask]         = {v[mask]}")       # keep only values > 3
print(f"v[v % 2 == 0]       = {v[v % 2 == 0]}") # inline - even values only