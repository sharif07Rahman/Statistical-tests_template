

# One Sample T-Test
'''In this code, we perform a one-sample t-test to determine if the mean of a sample from our generated
 population is statistically different from the population mean. The histograms help us visualize the distribution
 of the population and sample data, and the t-test compares the sample mean to the population mean, leading us to 
 either reject or not reject the null hypothesis based on the p-value.
'''

# Import required packages for data manipulation, statistical analysis, and plotting
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp,norm

# Generate a normally distributed population with a mean of 500, a standard deviation of 100, and a size of 1000
# The random state is set to 42 for reproducibility
population = norm.rvs(loc=500, scale=100, size=1000, random_state=42).astype(int)

# Seed the random number generator for reproducibility
np.random.seed(42)

# Randomly select 250 samples from the population for analysis
sample = np.random.choice(population, 250)

# Plot a histogram of the population and sample to visually inspect the distribution
plt.hist(population, density=True, alpha=0.5, label='Population')
plt.hist(sample, density=True, alpha=0.5, label='Sample')
plt.legend()
plt.show()

# Calculate the mean of the population and the sample to compare them
population_mean = population.mean()
sample_mean = sample.mean()
print("Population Mean:", population_mean, "Sample Mean:", sample_mean)

# Set the hypotheses and significance level for the t-test
# Null hypothesis: sample mean is equal to the population mean (no effect)
null_hypothesis = "The mean of the sample is equal to the mean of the population"
# Alternative hypothesis: sample mean is different from the population mean (effect exists)
alternate_hypothesis = "The mean of the sample is different to the mean of the population"
# Significance level: commonly set to 5% for such tests
acceptance_criteria = 0.05

# Execute the one-sample t-test comparing the sample mean against the population mean
t_statistic, p_value = ttest_1samp(sample, population_mean)
print("T-Statistic:", t_statistic, "P-value:", p_value)

"""# Evaluate and print the test results based on the p-value
if p_value <= acceptance_criteria:
    # If the p-value is less than or equal to the significance level, reject the null hypothesis
    print(f"As our p-value of {p_value} is lower than our acceptance criteria of {acceptance_criteria}, we reject the null hypothesis, and conclude that: {alternate_hypothesis}")
else:
    # If the p-value is greater, we do not reject the null hypothesis
    print(f"As our p-value of {p_value} is higher than our acceptance criteria of {acceptance_criteria}, we retain the null hypothesis, and conclude that: {null_hypothesis}")
"""



# Evaluate and print the test results based on the p-value
if p_value <= acceptance_criteria:
    # If the p-value is less than or equal to the significance level, reject the null hypothesis
    print("As our p-value of {} is lower than our acceptance criteria of {}, we reject the null hypothesis, and conclude that: {}".format(p_value, acceptance_criteria, alternate_hypothesis))
else:
    # If the p-value is greater, we do not reject the null hypothesis
    print("As our p-value of {} is higher than our acceptance criteria of {}, we retain the null hypothesis, and conclude that: {}".format(p_value, acceptance_criteria, null_hypothesis))
