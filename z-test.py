import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Conversion data for each group
# Format: [conversions_group_A, conversions_group_B]
conversions = np.array([50, 65])

# Sample sizes (number of visitors) for each group
sample_sizes = np.array([1000, 980])

# Perform two-sample z-test for proportions
z_stat, p_value = proportions_ztest(conversions, sample_sizes)

# Print results
print(f"Group A: {conversions[0]} conversions out of {sample_sizes[0]} visitors")
print(f"Group B: {conversions[1]} conversions out of {sample_sizes[1]} visitors")
print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.3f}")

if p_value < 0.05:
    print("Result: The difference is statistically significant")
else:
    print("Result: No statistically significant difference")
