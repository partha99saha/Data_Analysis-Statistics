import numpy as np
from scipy.stats import ttest_1samp
import matplotlib.pyplot as plt


# Generate a sample dataset (random data)
np.random.seed(42)  # for reproducibility
# generate 100 random samples from a normal distribution
data = np.random.normal(loc=50, scale=10, size=100)

# Statistical analysis
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
# correlation matrix for demonstration purposes (correlation of data with itself)
correlation_matrix = np.corrcoef(data, data)

print("Statistical Analysis:")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Correlation Matrix:")
print(correlation_matrix)

# Hypothesis testing
# (example: testing if the mean of the data is equal to a specific value)
# Let's assume null hypothesis H0: mean = 50
# We will use a significance level of 0.05
expected_mean = 50
t_statistic, p_value = ttest_1samp(data, expected_mean)

print("\nHypothesis Testing:")
print("T-statistic:", t_statistic)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis (H0) at 0.05 significance level.")
else:
    print("Fail to reject null hypothesis (H0) at 0.05 significance level.")

# Confidence interval estimation
# (example: estimating confidence interval for the mean of the data)
confidence_level = 0.95
n = len(data)
standard_error = np.std(data) / np.sqrt(n)
margin_of_error = standard_error * np.abs(
    np.percentile(
        np.random.normal(loc=0, scale=1, size=10000), (1 - confidence_level) * 100
    )
)
lower_bound = mean - margin_of_error
upper_bound = mean + margin_of_error

print("\nConfidence Interval Estimation:")
print("Confidence Level:", confidence_level)
print("Margin of Error:", margin_of_error)
print("Confidence Interval: [{:.2f}, {:.2f}]".format(lower_bound, upper_bound))

# ----------------- Visualization -----------------
plt.figure(figsize=(10, 6))

# Histogram
plt.hist(data, bins=15, color="skyblue", edgecolor="black", alpha=0.7)
plt.axvline(mean, color="red", linestyle="--", label=f"Mean = {mean:.2f}")
plt.axvline(
    lower_bound, color="green", linestyle="--", label=f"CI Lower = {lower_bound:.2f}"
)
plt.axvline(
    upper_bound, color="green", linestyle="--", label=f"CI Upper = {upper_bound:.2f}"
)

plt.title("Histogram of Sample Data with Mean and 95% Confidence Interval")
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(data, vert=True, patch_artist=True, boxprops=dict(facecolor="skyblue"))
plt.title("Boxplot of Sample Data")
plt.ylabel("Values")
plt.grid(True)
plt.show()
