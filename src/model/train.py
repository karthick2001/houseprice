import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from joblib import dump
from src.data.data_loader import load_data  # Import the load_data function

def train_model(data):
    # Define features and target
    X = data.drop(columns=['Price', 'id', 'Date'])
    y = data['Price']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    dump(model, 'model/housing_price_model.joblib')

    return model