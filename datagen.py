# Corrected approach to generate 50 more logical data points and write to a CSV file

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Base data for reference
base_data = {
    "Worker_ID": ["001", "002", "003", "004", "005"],
    "Date": ["2023-01-15", "2023-01-15", "2023-01-16", "2023-01-16", "2023-01-17"],
    "Time_Start": ["08:00:00", "09:00:00", "07:30:00", "08:00:00", "08:30:00"],
    "Time_End": ["16:00:00", "17:00:00", "15:30:00", "17:00:00", "16:30:00"],
    "Crop_Type": ["Wheat", "Corn", "Soybeans", "Wheat", "Corn"],
    "Base_Hourly_Wage": [12.00, 11.50, 12.50, 12.00, 11.50],
    "Supply_Demand_Ratio": [1.2, 1.3, 1.1, 1.2, 1.5],
    "Dynamic_Pricing_Multiplier": [1.44, 1.495, 1.375, 1.44, 1.725],
    "Total_Earnings": [138.24, 148.75, 137.50, 138.24, 172.50]
}

# Function to calculate total earnings
def calculate_earnings(hours, wage, multiplier):
    return hours * wage * multiplier

# Data generation parameters
num_new_data = 5000
crop_types = ["Wheat", "Corn", "Soybeans"]
supply_demand_ratios = [1.1, 1.2, 1.3, 1.4, 1.5]
multipliers = [1.375, 1.44, 1.495, 1.56, 1.625, 1.725]
base_hourly_wage = {"Wheat": 12.00, "Corn": 11.50, "Soybeans": 12.50}
date_range = pd.date_range(start="2023-01-18", periods=15).strftime('%Y-%m-%d').tolist()

# Generate new data
new_data = []
for i in range(num_new_data):

    date = np.random.choice(date_range)
    crop_type = np.random.choice(crop_types)
    start_time = datetime.strptime(np.random.choice(["08:00:00", "09:00:00", "07:30:00"]), '%H:%M:%S')
    end_time = (start_time + timedelta(hours=np.random.randint(8, 10))).strftime('%H:%M:%S')
    start_time = start_time.strftime('%H:%M:%S')
    supply_demand_ratio = np.random.choice(supply_demand_ratios)
    dynamic_pricing_multiplier = np.random.choice(multipliers)
    base_wage = base_hourly_wage[crop_type]
    hours_worked = (datetime.strptime(end_time, '%H:%M:%S') - datetime.strptime(start_time, '%H:%M:%S')).seconds / 3600
    total_earnings = calculate_earnings(hours_worked, base_wage, dynamic_pricing_multiplier)
    
    new_data.append([date, start_time, end_time, crop_type, base_wage, supply_demand_ratio, dynamic_pricing_multiplier, total_earnings])

# Create DataFrame for the new data
new_df = pd.DataFrame(new_data, columns=["Date", "Time_Start", "Time_End", "Crop_Type", "Base_Hourly_Wage", "Supply_Demand_Ratio", "Dynamic_Pricing_Multiplier", "Total_Earnings"])

# Save to CSV file
csv_path = "generated_worker_data.csv"
new_df.to_csv(csv_path, index=False)

csv_path
