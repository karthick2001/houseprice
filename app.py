from flask import Flask, request, render_template
from src.model.inference import predict_price

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        'No of bedrooms': int(request.form['bedrooms']),
        'No of bathrooms': int(request.form['bathrooms']),
        'living area': float(request.form['living_area']),
        'lot area': float(request.form['lot_area']),
        'No of floors': int(request.form['floors']),
        'waterfront present': int(request.form['waterfront']),
        'No of views': int(request.form['views']),
        'house condition': int(request.form['condition']),
        'house grade': int(request.form['grade']),
        'house area(excluding basement)': float(request.form['house_area']),
        'Area of the basement': float(request.form['basement_area']),
        'Built Year': int(request.form['built_year']),
        'Renovation Year': int(request.form['renovation_year']),
        'No of schools nearby': int(request.form['schools']),
        'Distance from the airport': float(request.form['airport_distance']),
    }

    prediction = predict_price(input_data)
    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
