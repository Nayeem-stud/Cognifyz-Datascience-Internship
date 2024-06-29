import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Dataset.csv')

# Calculate basic statistics for numerical columns
numerical_stats = df.describe()
print("Basic Statistical Measures for Numerical Columns:")
print(numerical_stats)

# Explore categorical variables
country_counts = df['Country Code'].value_counts()
city_counts = df['City'].value_counts()
cuisine_counts = df['Cuisines'].value_counts()


# Visualize distribution of 'Country Code'
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.title('Distribution of Country Codes')
plt.xlabel('Country Code')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate x-axis labels if there are many categories
plt.show()

# Visualize distribution of 'City'
plt.figure(figsize=(10, 6))
sns.barplot(x=city_counts.index, y=city_counts.values)
plt.title('Distribution of Cities')
plt.xlabel('City')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate x-axis labels if there are many categories
plt.show()

# Visualize distribution of 'Cuisines'
plt.figure(figsize=(10, 6))
sns.barplot(x=cuisine_counts.index, y=cuisine_counts.values)
plt.title('Distribution of Cuisines')
plt.xlabel('Cuisines')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate x-axis labels if there are many categories
plt.show()


top_cuisines = df['Cuisines'].value_counts().head(10)

print("Top cuisines with the highest number of restaurants:")
print(top_cuisines)

# Top cities with the highest number of restaurants
top_cities = df['City'].value_counts().head(10)

print("\nTop cities with the highest number of restaurants:")
print(top_cities)
