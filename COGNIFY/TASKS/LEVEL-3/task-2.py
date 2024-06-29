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

# Convert categorical variables to numerical
df['Has Table booking'] = df['Has Table booking'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Is delivering now'] = df['Is delivering now'].apply(lambda x: 1 if x == 'Yes' else 0)
df['Switch to order menu'] = df['Switch to order menu'].apply(lambda x: 1 if x == 'Yes' else 0)

# Handling missing values (if any)
df = df.dropna()

# Analyze the relationship between the type of cuisine and the restaurant's rating
cuisine_ratings = df[['Cuisines', 'Aggregate rating']]
cuisine_ratings['Cuisines'] = cuisine_ratings['Cuisines'].str.split(', ')
cuisine_ratings = cuisine_ratings.explode('Cuisines')

# Group by cuisine type and calculate the mean rating
cuisine_rating_mean = cuisine_ratings.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
cuisine_rating_mean = cuisine_rating_mean.sort_values(by='Aggregate rating', ascending=False)

# Plot the average rating per cuisine
plt.figure(figsize=(12, 8))
sns.barplot(x='Aggregate rating', y='Cuisines', data=cuisine_rating_mean.head(10))
plt.title('Top 10 Cuisines by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Cuisine')
plt.show()

# Identify the most popular cuisines based on the number of votes
cuisine_votes = df[['Cuisines', 'Votes']]
cuisine_votes['Cuisines'] = cuisine_votes['Cuisines'].str.split(', ')
cuisine_votes = cuisine_votes.explode('Cuisines')

# Group by cuisine type and calculate the total votes
cuisine_votes_total = cuisine_votes.groupby('Cuisines')['Votes'].sum().reset_index()
cuisine_votes_total = cuisine_votes_total.sort_values(by='Votes', ascending=False)

# Plot the most popular cuisines by number of votes
plt.figure(figsize=(12, 8))
sns.barplot(x='Votes', y='Cuisines', data=cuisine_votes_total.head(10))
plt.title('Top 10 Most Popular Cuisines by Number of Votes')
plt.xlabel('Number of Votes')
plt.ylabel('Cuisine')
plt.show()

# Determine if there are specific cuisines that tend to receive higher ratings
# Combining cuisine_rating_mean and cuisine_votes_total
cuisine_analysis = pd.merge(cuisine_rating_mean, cuisine_votes_total, on='Cuisines')

# Plot the relationship between average rating and number of votes for cuisines
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Votes', y='Aggregate rating', data=cuisine_analysis)
plt.title('Relationship between Number of Votes and Average Rating for Cuisines')
plt.xlabel('Number of Votes')
plt.ylabel('Average Rating')
plt.show()

# Display the top cuisines by average rating and by number of votes
print("Top 10 Cuisines by Average Rating:")
print(cuisine_rating_mean.head(10))
print("\nTop 10 Most Popular Cuisines by Number of Votes:")
print(cuisine_votes_total.head(10))
