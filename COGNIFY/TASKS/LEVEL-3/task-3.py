import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('dataset.csv')

# Display the first few rows of the dataframe
print(df.head())

# Basic data exploration
print(df.info())
print(df.describe())

# Feature engineering
# Convert categorical variables to numerical
df['Has Table booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Is delivering now'] = df['Is delivering now'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Switch to order menu'] = df['Switch to order menu'].apply(lambda x: 1 if x == 'Yes' else 0)

# Handling missing values (if any)
df = df.dropna()

# 1. Visualize the distribution of ratings using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=20, kde=True)
plt.title('Distribution of Aggregate Ratings')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

# 2. Compare the average ratings of different cuisines using a bar plot
cuisine_ratings = df[['Cuisines', 'Aggregate rating']]
cuisine_ratings['Cuisines'] = cuisine_ratings['Cuisines'].str.split(', ')
cuisine_ratings = cuisine_ratings.explode('Cuisines')

# Group by cuisine type and calculate the mean rating
cuisine_rating_mean = cuisine_ratings.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
cuisine_rating_mean = cuisine_rating_mean.sort_values(by='Aggregate rating', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='Aggregate rating', y='Cuisines', data=cuisine_rating_mean.head(10))
plt.title('Top 10 Cuisines by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine')
plt.show()

# 3. Compare the average ratings of different cities using a bar plot
city_rating_mean = df.groupby('City')['Aggregate rating'].mean().reset_index()
city_rating_mean = city_rating_mean.sort_values(by='Aggregate rating', ascending=False)

plt.figure(figsize=(12, 8))
sns.barplot(x='Aggregate rating', y='City', data=city_rating_mean.head(10))
plt.title('Top 10 Cities by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('City')
plt.show()

# 4. Visualize the relationship between various features and the target variable
# Scatter plot for 'Average Cost for two' vs 'Aggregate rating'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Average Cost for two', y='Aggregate rating', data=df)
plt.title('Relationship between Average Cost for two and Aggregate Rating')
plt.xlabel('Average Cost for two')
plt.ylabel('Aggregate Rating')
plt.show()

# Box plot for 'Price range' vs 'Aggregate rating'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Price range', y='Aggregate rating', data=df)
plt.title('Relationship between Price Range and Aggregate Rating')
plt.xlabel('Price Range')
plt.ylabel('Aggregate Rating')
plt.show()

# Box plot for 'Has Table booking' vs 'Aggregate rating'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Has Table booking', y='Aggregate rating', data=df)
plt.title('Relationship between Table Booking and Aggregate Rating')
plt.xlabel('Has Table Booking')
plt.ylabel('Aggregate Rating')
plt.show()

# Box plot for 'Has Online delivery' vs 'Aggregate rating'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Has Online delivery', y='Aggregate rating', data=df)
plt.title('Relationship between Online Delivery and Aggregate Rating')
plt.xlabel('Has Online Delivery')
plt.ylabel('Aggregate Rating')
plt.show()
