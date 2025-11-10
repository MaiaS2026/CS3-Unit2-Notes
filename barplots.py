import pandas as pd
from matplotlib import pyplot as plt

# Data
languages = {
    'lang': ['Spanish', 'French', 'Mandarin', 'English'],
    'speakers': [5, 2, 2, 8],
    'difficulty': [1, 3, 10, 1]
}

# Turn dictionary into dataframe
df = pd.DataFrame(languages)

# Bar charts are great for COUNTS
# often use String data for the labels
df_sorted = df.sort_values(by='speakers', ascending=False)
colors = ['blue', 'yellow', 'green', 'red']
plt.bar(df_sorted['lang'], df_sorted['speakers'], color=colors, width=0.6)

# Often need to rotate labels on x axis for readability
plt.xticks(rotation=45)
plt.xlabel('Language')
plt.ylabel('Count of Speakers')
plt.title('Speakers of each Language')

plt.savefig('barchart.png', bbox_inches='tight')
plt.close()

# PIE CHARTS - to show parts of a whole/breakdown of a total
plt.pie(df['speakers'], labels=df['lang'].tolist(), startangle=270)

plt.savefig('piechart.png', bbox_inches='tight')


