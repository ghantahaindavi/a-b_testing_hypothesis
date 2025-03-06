import pandas as pd
from scipy import stats

# Load dataset
data = pd.read_csv('../datasets/sample_data.csv')

# Perform A/B Testing
group_A = data[data['group'] == 'A']['metric']
group_B = data[data['group'] == 'B']['metric']
t_stat, p_value = stats.ttest_ind(group_A, group_B)

print(f'T-Statistic: {t_stat}, P-Value: {p_value}')
