#A/B testing of mailing campaign to clients of two groups

                                                                        
import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Import data
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name="campaign_data")

# Filter data to exclude 'Control' mailer type
campaign_data_filtered = campaign_data[campaign_data["mailer_type"] != "Control"]

# Create a contingency table (crosstab) for observed frequencies
observed_values = pd.crosstab(campaign_data_filtered["mailer_type"], campaign_data_filtered["signup_flag"]).values

# Calculate signup rates for each mailer type
# Assuming mailer types are in a specific order in the crosstab, e.g., Mailer1 is first, Mailer2 is second
mailer1_signup_rate = observed_values[0][1] / sum(observed_values[0])  # Signup rate for Mailer1
mailer2_signup_rate = observed_values[1][1] / sum(observed_values[1])  # Signup rate for Mailer2

# Print the signup rates
print(mailer1_signup_rate, mailer2_signup_rate)

#HYPOTHESIS AND ACCEPTANCE CRITERIA
null_hypothesis = "there is no relationship between mailer type and signup rate. They are independent"
alternative_hypothesis = "there is relationship between mailer type and signup rate. They are not independent"
acceptance_criteria= 0.05

# Calculate acceptance criteria and Chi square stats
chi2_statistic,p_value, dof, expected_values= chi2_contingency(observed_values, correction =False) 
print(chi2_statistic, p_value)

#Critical value
'''chi2.ppf(1 - acceptance_criteria, dof) calculates the critical value of the chi-square 
statistic such that the area under the chi-square distribution curve to the right of this value equals
the significance level (acceptance_criteria).
'''
critical_value= chi2.ppf(1- acceptance_criteria, dof)
print(critical_value)

#print chi2 statistic result
if chi2_statistic >= critical_value:
    print(f"Since the Chi-square statistic of {chi2_statistic} is higher than that of the critical value of {critical_value}: We reject the null hypothesis and conclude that {alternative_hypothesis}.")
else:
    print(f"Since the Chi-square statistic of {chi2_statistic} is lower than that of the critical value of {critical_value}: We retain the null hypothesis and conclude that {null_hypothesis}.")

#print p-value  result
if p_value <= acceptance_criteria:
    print(f"Since the p-value of {p_value} is lower than that of the aceptance_criteria of {acceptance_criteria}: We reject the null hypothesis and conclude that {alternative_hypothesis}.")
else:
    print(f"Since the p-value of {p_value} is higher than that of the aceptance_criteria of {acceptance_criteria}: We retain the null hypothesis and conclude that {null_hypothesis}.")






















