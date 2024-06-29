import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load your dataset (replace 'dataset.csv' with your actual file path)
df = pd.read_csv('Dataset.csv')

# Task 1: Determine the most common price range
most_common_price_range = df['Price range'].mode()[0]
print(f"Most common price range among all restaurants: {most_common_price_range}")

# Task 2: Calculate average rating for each price range
average_rating_by_price_range = df.groupby('Price range')['Aggregate rating'].mean().sort_index()

print("\nAverage rating for each price range:")
print(average_rating_by_price_range)

# Task 3: Identify the color representing the highest average rating
highest_rating_color = sns.color_palette("viridis", as_cmap=True)(average_rating_by_price_range.idxmax())
print(f"\nColor representing the highest average rating: {highest_rating_color}")

# Optional: Visualize average rating by price range
plt.figure(figsize=(10, 6))
sns.barplot(x=average_rating_by_price_range.index, y=average_rating_by_price_range.values, palette="viridis")
plt.title('Average Rating by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
