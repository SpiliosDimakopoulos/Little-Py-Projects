import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:

    if n <= 0:
        return pd.DataFrame({f'getNthHighestSalary({n})': [None]})
    
    result = employee.sort_values(
        by='salary',
        ascending=False,
    ).drop_duplicates(
        subset=['salary'],
    ).iloc[n - 1:n][['salary']]
    
    if result.empty:
        return pd.DataFrame({f'getNthHighestSalary({n})': [None]})
    
    return result.rename(columns={'salary': f'getNthHighestSalary({n})'})
