# ============================================
# MSCS Data Analysis Assignment - Result Checker
# ============================================

import math
import statistics

print("\n========== PART 1: DESCRIPTIVE STATISTICS ==========")

ages = [12, 14, 14, 17, 18, 19, 20, 21, 21, 23, 24, 24, 26,
        28, 30, 32, 33, 34, 36, 38, 40, 42, 44, 45, 50, 55, 60]

print("Dataset (Ages):", ages)
print("Count:", len(ages))
print("Mean:", sum(ages) / len(ages))
print("Median:", statistics.median(ages))
print("Mode(s):", statistics.multimode(ages))
print("Min:", min(ages))
print("Max:", max(ages))
print("Midrange:", (min(ages) + max(ages)) / 2)

q1 = statistics.quantiles(ages, n=4)[0]
q3 = statistics.quantiles(ages, n=4)[2]

print("Q1:", q1)
print("Q3:", q3)

print("\nFive-Number Summary:")
print("Minimum:", min(ages))
print("Q1:", q1)
print("Median:", statistics.median(ages))
print("Q3:", q3)
print("Maximum:", max(ages))


print("\n========== PART 2: DISTANCE METRICS ==========")

p1 = (18, 3, 40, 12)
p2 = (25, 2, 38, 15)

print("Point A:", p1)
print("Point B:", p2)

# Euclidean Distance
euclidean = math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))
print("Euclidean Distance:", euclidean)

# Manhattan Distance
manhattan = sum(abs(a - b) for a, b in zip(p1, p2))
print("Manhattan Distance:", manhattan)

# Minkowski Distance (q = 4)
q = 4
minkowski = sum(abs(a - b) ** q for a, b in zip(p1, p2)) ** (1 / q)
print("Minkowski Distance (q=4):", minkowski)

# Supremum (Chebyshev) Distance
supremum = max(abs(a - b) for a, b in zip(p1, p2))
print("Supremum (Chebyshev) Distance:", supremum)


print("\n========== PART 3: DATA SMOOTHING & OUTLIERS ==========")

data = [12, 14, 15, 18, 19, 20, 22, 22, 23, 24, 26, 27, 27, 28,
        30, 31, 33, 35, 36, 36, 37, 38, 40, 42, 44, 50, 53, 75]

print("Dataset:", data)

# Binning (Bin size = 4)
bin_size = 4
bins = [data[i:i + bin_size] for i in range(0, len(data), bin_size)]

print("\nBins and Bin Means:")
for i, b in enumerate(bins, start=1):
    mean = sum(b) / len(b)
    print(f"Bin {i}: {b} -> Mean = {mean}")

# IQR Outlier Detection
q1 = statistics.quantiles(data, n=4)[0]
q3 = statistics.quantiles(data, n=4)[2]
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = [x for x in data if x < lower_bound or x > upper_bound]

print("\nIQR Method Results:")
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", outliers)


print("\n========== PART 4: NORMALIZATION ==========")

values = [150, 250, 350, 500, 800]
print("Original Values:", values)

# Min-Max Normalization
min_val = min(values)
max_val = max(values)
min_max = [(x - min_val) / (max_val - min_val) for x in values]
print("\nMin-Max Normalization (0 to 1):", min_max)

# Z-score Normalization (Standard Deviation)
mean = statistics.mean(values)
std = statistics.stdev(values)
z_scores_std = [(x - mean) / std for x in values]
print("Z-score Normalization (Std Dev):", z_scores_std)

# Z-score Normalization (Mean Absolute Deviation)
mad = sum(abs(x - mean) for x in values) / len(values)
z_scores_mad = [(x - mean) / mad for x in values]
print("Z-score Normalization (MAD):", z_scores_mad)

# Decimal Scaling
decimal_scaling = [x / 1000 for x in values]
print("Decimal Scaling:", decimal_scaling)


print("\n========== END OF ASSIGNMENT CHECK ==========")
