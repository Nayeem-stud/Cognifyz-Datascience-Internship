import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('Dataset.csv')

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

# Selecting features and target variable
features = ['Average Cost for two', 'Has Table booking', 'Has Online delivery', 'Is delivering now', 'Price range']
target = 'Aggregate rating'

X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Dictionary to store models and their performance
models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(random_state=42),
    'Random Forest Regressor': RandomForestRegressor(random_state=42)
}

# Train and evaluate each model
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f'{name} - Mean Squared Error: {mse}, R-squared: {r2}')
