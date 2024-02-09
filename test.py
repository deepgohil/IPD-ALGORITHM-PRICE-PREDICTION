import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the path to your dataset

# Data Preprocessing
data['Duration'] = (pd.to_datetime(data['Time_End']) - pd.to_datetime(data['Time_Start'])).dt.total_seconds() / 3600

# Feature Engineering
# Convert categorical variables to numerical representations (one-hot encoding)
data = pd.get_dummies(data, columns=['Crop_Type'])

# Normalize numerical variables
scaler = StandardScaler()
data[['Base_Hourly_Wage', 'Supply_Demand_Ratio', 'Duration', 'Total_Earnings']] = scaler.fit_transform(data[['Base_Hourly_Wage', 'Supply_Demand_Ratio', 'Duration', 'Total_Earnings']])

# Model Training
X = data[['Base_Hourly_Wage', 'Supply_Demand_Ratio', 'Duration', 'Crop_Type_Corn', 'Crop_Type_Soybeans', 'Crop_Type_Wheat']]
y = data['Dynamic_Pricing_Multiplier']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Model Deployment: Deploy the trained model for dynamic pricing calculations
# You can use 'model.predict()' to predict the dynamic pricing multiplier for new data
