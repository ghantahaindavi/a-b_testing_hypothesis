import pandas as pd
from scipy import stats

# Load dataset
data = pd.read_csv('../datasets/sample_data.csv')

# Perform Chi-Square Test
contingency_table = pd.crosstab(data['category'], data['outcome'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print(f'Chi-Square: {chi2}, P-Value: {p}')
