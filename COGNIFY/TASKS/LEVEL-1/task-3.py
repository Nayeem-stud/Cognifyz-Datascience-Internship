import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset from CSV file
df = pd.read_csv('Dataset.csv')

# Task 1: Plotting Restaurant Locations
if 'Longitude' in df.columns and 'Latitude' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Longitude'], df['Latitude'], alpha=0.5)
    plt.title('Restaurant Locations')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.show()
else:
    print("Error: 'Longitude' or 'Latitude' columns not found in the dataset.")

# Task 2: Plotting Restaurant Distribution by City
if 'City' in df.columns:
    city_counts = df['City'].value_counts()
    plt.figure(figsize=(12, 6))
    city_counts.plot(kind='bar', title='Restaurant Distribution by City')
    plt.xlabel('City')
    plt.ylabel('Number of Restaurants')
    plt.show()
else:
    print("Error: 'City' column not found in the dataset.")

# Task 3: Plotting Restaurant Distribution by Country
if 'Country Code' in df.columns:
    country_counts = df['Country Code'].value_counts()
    plt.figure(figsize=(14, 8))
    country_counts.plot(kind='pie', title='Restaurant Distribution by Country Code')
    plt.ylabel('')
    plt.show()
else:
    print("Error: 'Country Code' column not found in the dataset.")

# Task 4: Plotting Restaurant Locations and Ratings
if 'Aggregate rating' in df.columns:
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Longitude', y='Latitude', hue='Aggregate rating', data=df, palette='coolwarm')
    plt.title('Restaurant Locations and Ratings')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(title='Aggregate rating')
    plt.show()
else:
    print("Error: 'Aggregate rating' column not found in the dataset.")