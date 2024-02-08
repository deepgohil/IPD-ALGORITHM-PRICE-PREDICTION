from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

# Data preparation
# Combine the base data with new data for the full dataset
full_data = pd.read_csv("generated_worker_data.csv")

# Feature engineering
# Convert 'Date' to datetime and extract useful features
full_data['Date'] = pd.to_datetime(full_data['Date'])
full_data['Day_of_Week'] = full_data['Date'].dt.dayofweek
full_data['Month'] = full_data['Date'].dt.month

# Calculate working hours from 'Time_Start' and 'Time_End'
full_data['Working_Hours'] = (pd.to_datetime(full_data['Time_End']) - pd.to_datetime(full_data['Time_Start'])).dt.seconds / 3600

# Select features and target
X = full_data[['Day_of_Week', 'Month', 'Working_Hours', 'Crop_Type', 'Base_Hourly_Wage', 'Supply_Demand_Ratio', 'Dynamic_Pricing_Multiplier']]
y = full_data['Total_Earnings']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing: One-hot encoding for categorical data and standardization for numerical data
numerical_features = ['Day_of_Week', 'Month', 'Working_Hours', 'Base_Hourly_Wage', 'Supply_Demand_Ratio', 'Dynamic_Pricing_Multiplier']
categorical_features = ['Crop_Type']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Define the ANN model
ann_model = MLPRegressor(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=500, random_state=42)

# Create a pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', ann_model)])

# Train the model
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

mse, r2
