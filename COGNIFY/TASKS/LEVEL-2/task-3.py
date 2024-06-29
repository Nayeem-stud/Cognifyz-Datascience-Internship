
import pandas as pd

# Load your dataset (replace 'dataset.csv' with your actual file path)
df = pd.read_csv('Dataset.csv')

# Example: Extracting additional features
df['Restaurant name length'] = df['Restaurant Name'].apply(lambda x: len(str(x)))
df['Address length'] = df['Address'].apply(lambda x: len(str(x)))

# Example: Creating new features by encoding categorical variables
df['Has Table Booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})  # Example: If 'Has Table booking' is categorical
df['Has Online Delivery'] = df['Has Online delivery'].map({True: 1, False: 0})  # Example: If 'Has Online delivery' is boolean

# Print or inspect the modified DataFrame with new features
print(df.head())

# Save the updated DataFrame to a new CSV file if needed
df.to_csv('updated_dataset.csv', index=False)
