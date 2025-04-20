import numpy as np

# 1. Create a range of numbers
a = np.arange(12)
print("1D Array", a)

# 2. Reshapre it to 3 rows x 4 columns
a2 = a.reshape(3, 4)
print("Reshapred (3x4):\n", a2)

# 3. index: get elemt from row 1, column2
print("elemnt at [1,2]:", a2[1, 2])

# 4. Slice: get all values from column 1
print("Column 1:", a2[:, 1])

# 5. create zeros and ones
print("Zeros:", np.zeros(5))
print("Ones (2x3):\n", np.ones((2,3)))
      
# 6. filter: Numbers greater than 5
print("Greater than 5:", a[a>5])