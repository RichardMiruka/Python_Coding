# Why list comprehensions are faster than using traditional for loops because they optimized for performance

# List comprehensions are more efficient than using for loops because they use less memory and are faster to execute.
# They are also more readable and easier to understand than for loops.

# List comprehensions are optimized for performance because they use less memory and are faster to execute.

import time 

# Using for loops - Traditional approach
start_time = time.time()
result = []
for i in range(1000000):
    result.append(i * 2)
end_time = time.time()
print("Using for loops:", end_time - start_time)

# Using list comprehensions
start_time = time.time()
result = [i * 2 for i in range(1000000)]
end_time = time.time()
print("Using list comprehensions:", end_time - start_time)
