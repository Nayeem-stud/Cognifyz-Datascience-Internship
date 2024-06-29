import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Dataset.csv')

# Get the shape of the DataFrame
rows, cols = df.shape
print(f'The dataset has {rows} rows and {cols} columns.')

# Check for missing values in each column
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# Handle missing values by filling with mean (only for numeric columns)
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Plot distribution of Aggregate Rating
plt.figure(figsize=(10, 6))
sns.histplot(df['Aggregate rating'], bins=20, kde=True)
plt.title('Distribution of Aggregate Rating')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.show()

# Get the count of each rating
rating_counts = df['Aggregate rating'].value_counts()

# Print the counts for each rating
print('Counts for each Aggregate Rating:')
print(rating_counts)

if 'Category' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Category', data=df, palette='Set3')
    plt.title('Count of Categories')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.show()
