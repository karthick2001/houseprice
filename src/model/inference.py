from joblib import load
import pandas as pd

def predict_price(input_data):
    # Load the trained model
    model = load('model/housing_price_model.joblib')

    # Prepare input data (ensure it's in the right format)
    input_df = pd.DataFrame(input_data, index=[0])  # Create DataFrame with a single row
    prediction = model.predict(input_df)

    return prediction[0]  # Return the single prediction
