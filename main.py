import numpy as np
import pandas as pd

# Seroes object is a 1D array of indexed data 
# Like a COLUMN (one category)
month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', "Oct", 'Nov', 'Dec'])
print(month)
# Series have attributes values & index
print(month.values) # looks like a list
print(month.index) #shows the range of nums

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', "Jul", 'Aug', 'Sep', "Oct", 'Nov', 'Dec']
better_month = pd.Series(month_list, index=[1,2,3,4,5,6,7,8,9,10,11,12])
print(f"My birthday is in {better_month[4]}")

birth_months = {'Kevin':'Mar',
                'Jackson':'Aug',
                'Finny':'Jul',
                'Bryce':'Nov',
                'Natalie':'Mar',
                'Paige':'Feb',
                'Maia':'Apr'}
birth_series = pd.Series(birth_months)
print(birth_series)