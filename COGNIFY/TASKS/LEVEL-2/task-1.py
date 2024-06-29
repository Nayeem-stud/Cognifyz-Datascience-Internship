import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset 
df = pd.read_csv('Dataset.csv')

# Convert 'Has Table booking' and 'Has Online delivery' to boolean
df['Has Table booking'] = df['Has Table booking'].astype(bool)
df['Has Online delivery'] = df['Has Online delivery'].astype(bool)

# Task 1: Determine the percentage of restaurants that offer table booking and online delivery
total_restaurants = len(df)
restaurants_with_table_booking = df['Has Table booking'].sum()
restaurants_with_online_delivery = df['Has Online delivery'].sum()

percentage_table_booking = (restaurants_with_table_booking / total_restaurants) * 100
percentage_online_delivery = (restaurants_with_online_delivery / total_restaurants) * 100

print(f"Percentage of restaurants that offer table booking: {percentage_table_booking:.2f}%")
print(f"Percentage of restaurants that offer online delivery: {percentage_online_delivery:.2f}%")

# Task 2: Compare the average ratings of restaurants with table booking and those without
avg_rating_with_booking = df[df['Has Table booking']]['Aggregate rating'].mean()
avg_rating_without_booking = df[~df['Has Table booking']]['Aggregate rating'].mean()

print(f"\nAverage rating of restaurants with table booking: {avg_rating_with_booking:.2f}")
print(f"Average rating of restaurants without table booking: {avg_rating_without_booking:.2f}")

# Task 3: Analyze availability of online delivery among restaurants with different price ranges
availability_by_price_range = df.groupby('Price range')['Has Online delivery'].mean() * 100

print("\nOnline delivery availability by price range:")
print(availability_by_price_range)

# Optional: Visualize availability by price range
plt.figure(figsize=(10, 6))
sns.barplot(x=availability_by_price_range.index, y=availability_by_price_range.values)
plt.title('Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Percentage with Online Delivery')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
