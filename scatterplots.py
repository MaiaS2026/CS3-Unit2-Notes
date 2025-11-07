import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

plt.style.use('seaborn-v0_8-dark')
print(plt.style.available)

# Read CSV file into Pandas DataFrame
cities = pd.read_csv('california_cities.csv')
print(cities.info()) # look at columns, dtypes, entries

# Extract data columns for our scatterplot
latitudes = cities['latd'] # y values
longitudes = cities['longd'] # x values
populations = cities['population_total']
area = cities['area_total_sq_mi']

# Generate scatterplot (each city row is a dot)
plt.scatter(longitudes, latitudes, s=area, c=populations, cmap='plasma')

plt.title('California Cities')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.axis('equal')

plt.savefig('scatter-cities.png')
plt.close()

# Scatterplot from Iriis dataset (machine learning)
iris = load_iris()
print(iris) # 'feature_names': ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
features = iris.data.T # transpose (switch rows and cols)

plt.scatter(features[0], features[1], c=iris.target, cmap='viridis', alpha=0.5, s=features[3]*100)
# Use column names as labels
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.savefig('scatter-iris.png')