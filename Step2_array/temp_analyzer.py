import numpy as np

# step 1: Create an array of tempratures
temps = np.array([17, 21, 19, 22, 20, 18, 23])

# Step2: Calculate average temprature
avg_temp = np.mean(temps)

# Step 3: Get max and min
max_temp = np.max(temps)
min_temp = np.min(temps)

# Step 4: Fidn temps  above average
above_avg = temps[temps > avg_temp]

# Print Results
print("Average temprature:", avg_temp)
print("Max temprature:", max_temp)
print("Min temprature:", min_temp)
print("Temperatures above average:", above_avg)
