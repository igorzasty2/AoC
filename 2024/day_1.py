import numpy as np
from collections import Counter
# Setup

data = np.loadtxt('data/day_1.txt').T
row1, row2 = sorted(map(int, data[0])), sorted(map(int, data[1]))

# Part 1

sol = sum(abs(a - b) for a, b in zip(row1, row2))
print(f"Distance: {sol}")

# Part 2
row2_count = Counter(row2)
sol = sum(row2_count[a]*a for a in row1)
print(f"Occurences: {sol}")