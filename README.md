-Comparison of T-Tests: Understanding the Differences Through Examples-
T-tests are a family of hypothesis tests that allow us to compare means and determine if differences are statistically significant. The type of t-test you choose depends on the data structure and the hypothesis you're testing. Here's an overview of various t-tests with examples:

-One-Sample T-Test:
Purpose: To determine if the mean of a single group is different from a known or hypothesized population mean.
Example: A researcher wants to know if the average height of a sample of 50 basketball players is different from the general population average of 6 feet. The one-sample t-test will compare the sample mean against the population mean.
-Independent Two-Sample T-Test:
Purpose: To compare the means of two unrelated groups on the same dependent variable.
Example: Comparing the average scores of two different classrooms (Group A and Group B) on a standardized test to see if one group's mean score differs significantly from the other.
-Paired Sample T-Test (Dependent T-Test)
Purpose: To compare the means of the same group at two different times or under two different conditions.
Example: Measuring the blood pressure of patients before and after a treatment to determine if the treatment led to significant changes in blood pressure.
-Welch’s T-Test
Purpose: An adaptation of the independent t-test used when the two groups have unequal variances and sample sizes.
Example: Comparing the average processing time of two customer service teams with different training programs, where one team is much larger and has more variance in their times.
-Other Variants
-Repeated Measures ANOVA: An extension of the paired sample t-test when comparing more than two time points or conditions.
-Two-Sample T-Test Assuming Equal Variances: Used when the variances of the two groups are statistically similar, unlike in Welch's.
-One-Way ANOVA: Used to compare the means across three or more unrelated groups.
Each of these tests is used in specific scenarios that depend on the distribution of data, whether samples are independent or related, and if the groups have equal variances and sizes.

--------------------------------
--------------------------------

#A/B testing of mailing campaign to clients of two groups
"""
A/B Testing for Mailing Campaign Analysis:
This repository contains a Python script for conducting A/B testing on a grocery store mailing campaign. The analysis aims to determine if 
there's a statistically significant difference in signup rates between two different types of mailers sent to clients.

Overview:
The script uses a dataset from a grocery_database.xlsx file, specifically from the campaign_data sheet. It filters out control group data
to focus on the active mailer types. Using the pandas library for data manipulation and the scipy.stats module for statistical analysis,
it sets up a contingency table and computes the Chi-square statistic and p-value to test the independence of mailer types and signup rates.

Hypothesis Testing:
The null hypothesis states there is no relationship between the mailer type and the signup rate (i.e., they are independent). The alternative
hypothesis posits that a relationship exists, indicating the mailer type influences the signup rate. The script calculates the Chi-square statistic
and compares it against a critical value at a significance level of 0.05 to determine whether to retain or reject the null hypothesis.

Results:
The script prints out the signup rates for each mailer type, the Chi-square statistic, p-value, and the critical value. It concludes the results 
of the hypothesis test based on the calculated statistics and the defined acceptance criteria.
"""
