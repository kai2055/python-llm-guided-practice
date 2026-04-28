
import numpy as np

arr = np.arange(12).reshape(3,4)
print("original:\n", arr)

# Slice - view
view = arr[0:2, 1:3]
print("\nView before mutation:\n", view)
view[0,0] = 999
print("Original after mutating view:\n", arr)

# Boolean index - copy
mask = arr > 5
copy = arr[mask]
print("\ncopy (1D from boolean index:\n)", copy)
copy[0] = -1
print("original unchanged after mutating copy:\n", arr)

# Check ownership
arr2 = np.arange(6)
s = arr2[1:4]
print("\nslice base is arr2:", s.base is arr2)

b = arr2[arr2 > 2]
print("boolean index base is None (owns data):", b.base is None)
