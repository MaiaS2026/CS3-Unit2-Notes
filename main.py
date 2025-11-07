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

# Create a DataFrame from a single Series object
df = pd.DataFrame(birth_series, columns=['Birth Month'])
print(df)

# Load tabulae data from a csv file into a dataframe
pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df) # [800 rows x 12 display cols]
print(pokemon_df.columns) # display col headers
# Column headers can be used to access individual columns
print(pokemon_df['Name'])
# Shortcut using DOT OPERATOR notation
print(pokemon_df.HP)
print(pokemon_df['Type 1'])

# Add a new column
pokemon_df['Attack Ratio'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

# Examples of getting info about a DataFrame
print(pokemon_df.head(10)) # shows first n rows
print(pokemon_df.sample(3)) # show random sample of n rows
#print(pokemon_df.shape_) # returns a tiple (rows, cols)
print(pokemon_df.columns) # returns a list of column headers
print(pokemon_df.info()) # shows non-null count & dtypes
print(pokemon_df.describe()) 

# GROUPBY function helps you isolate groups of entries
print(pokemon_df.groupby('Type 1') [ ['HP', 'Speed'] ] )

# Create a new column with a sum of stat values
pokemon_df['Total'] = pokemon_df[ ['HP', 'Attack', 'Defense', 'Speed'] ].sum(axis=1)
print(pokemon_df['Total'])

# Use .groupby to identify average total stats by generation
print(pokemon_df.groupby('Generation')['Total'].mean() )

# Look at average total stats for legendary pokemon instead
print(pokemon_df.groupby('Legendary')['Total'].mean() )

# CONDITIONAL FILTERING
# pulling entries (rows) from the df that meet a condition

# Select pokemon with high HP values
subset1 = pokemon_df[ (pokemon_df['HP'] > 100) ]
print(subset1)

# Select Phychic-type pokemon only
subset2 = pokemon_df[ (pokemon_df['Type 1'] == 'Psychic') ]
print(subset2)
# creates a smaller dataframe from the original one

# Can also use MULTIPLE conditions (use the & for AND, the | for OR)
subset3 = subset2[ (subset2['Type 2'] == 'Fairy') & (subset2['Sp. Atk'] > 50) ]
print(subset3)

# Select pokemon whose name contains "Mega"
subset4 = pokemon_df[ pokemon_df['Name'].str.contains('Mega') ]
print(subset4)

# Exclude Legendary pokemon
subset5 = pokemon_df[ pokemon_df['Legendary'] == False ]
print(subset5)
# SHORTCUT wiyh this ~ operator (NOT)
subset6 = pokemon_df[ ~pokemon_df['Legendary'] ]
print(subset6)

