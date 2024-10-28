import pandas as pd
file_path=r"C:/Users/Windows/Desktop/projects/House Price India.csv"
def load_data(file_path):
    # Load dataset
    data = pd.read_csv(file_path)

    # Handle missing values
    data.fillna(method='ffill', inplace=True)

    # Convert categorical variables to numerical
    categorical_cols = ['waterfront present', 'house condition', 'house grade']
    data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

    # Normalize numerical features if necessary
    numerical_cols = ['living area', 'lot area', 'No of floors', 'No of views', 
                      'house area(excluding basement)', 'Area of the basement', 
                      'Built Year', 'Renovation Year', 'No of schools nearby', 
                      'Distance from the airport']
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()

    return data


