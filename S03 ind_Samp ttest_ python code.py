"""


"""
# Independent Samples T-Test

# Import required libraries
# numpy for numerical operations
# matplotlib.pyplot for plotting histograms
# scipy.stats for statistical tests
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

# Generate two independent samples with normal distributions
# np.random.normal generates random samples from a normal (Gaussian) distribution
# loc is the mean ('center') of the distribution
# scale is the standard deviation (spread or 'width') of the distribution
# size is the number of samples
# random_state ensures reproducibility

# Sample A is centered at 500 with a standard deviation of 100
sample_A = norm.rvs(loc=500, scale=100, size=250, random_state=42).astype(int)
# Sample B is centered at 550 with a standard deviation of 100
sample_B = norm.rvs(loc=550, scale=100, size=100, random_state=42).astype(int)

# Plot histograms to visualize the distributions of both samples
plt.hist(sample_A, density=True, alpha=0.5, label='Sample A')
plt.hist(sample_B, density=True, alpha=0.5, label='Sample B')
plt.legend()
plt.show()

# Calculate and print the means of both samples
sample_A_mean = sample_A.mean()
sample_B_mean = sample_B.mean()
print("Sample A Mean:", sample_A_mean, "Sample B Mean:", sample_B_mean)

# Set the hypotheses and acceptance criteria
# Null hypothesis: there is no difference in the means of the two samples
null_hypothesis = "The mean of Sample A is equal to the mean of Sample B"
# Alternative hypothesis: there is a difference in the means of the two samples
alternate_hypothesis = "The mean of Sample A is different from the mean of Sample B"
# Acceptance criteria is typically set at 0.05 for a 5% significance level
acceptance_criteria = 0.05

# Execute the independent t-test between the two samples
# ttest_ind performs a test on the means of two independent samples
t_statistic, p_value = ttest_ind(sample_A, sample_B)
print("T-Statistic:", t_statistic, "P-value:", p_value)

# Print the results based on the p-value
# Compare the p-value against the acceptance criteria to decide whether to reject the null hypothesis
if p_value < acceptance_criteria:
    # A p-value lower than the acceptance criteria suggests significant difference
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis and conclude that: {alternate_hypothesis}")
else:
    # A p-value higher suggests insufficient evidence to reject the null hypothesis
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we retain the null hypothesis and conclude that: {null_hypothesis}")



"""
IN this code:
-We first generate two sets of data representing our independent samples, each with their own mean and standard deviation.
-We then plot these distributions to visually inspect them.
-We calculate the means of each sample to get an idea of where they stand relative to one another.
-We set up our null and alternative hypotheses, which are statements about the population means that we are testing.
-We conduct the independent samples t-test, which calculates a t-statistic and produces a p-value. The t-statistic measures the size of the difference relative to the variation in our sample data. The smaller the p-value, the stronger the evidence we have to reject the null hypothesis.
-Finally, we interpret the results by comparing the p-value to our predetermined significance level (alpha). If the p-value is less than alpha, we have evidence to reject the null hypothesis in favor of the alternative; if it's greater, we do not have enough evidence to do so.
-The test helps us determine if the observed difference in sample means is likely to reflect a real difference in the population means or if it could be due to random chance alone.

"""