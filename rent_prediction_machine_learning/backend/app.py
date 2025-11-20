from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

# Prototype Data 
prototype_data = pd.DataFrame({
    'bedrooms': [1, 2, 2, 3, 3, 4, 1, 2, 3, 4, 2, 3, 1, 2, 4, 3, 2, 1, 3, 4],
    'bathrooms': [1, 1, 2, 2, 2, 3, 1, 1, 2, 2, 2, 2, 1, 1, 3, 2, 2, 1, 3, 3],
    'sqft': [600, 850, 900, 1200, 1300, 1800, 550, 800, 1150, 1750, 950, 1250, 580, 820, 1850, 1280, 880, 620, 1400, 1900],
    'location': ['downtown', 'suburb', 'downtown', 'suburb', 'downtown', 'suburb', 
                 'downtown', 'suburb', 'downtown', 'suburb', 'downtown', 'suburb',
                 'downtown', 'suburb', 'downtown', 'suburb', 'downtown', 'suburb', 'downtown', 'suburb'],
    'property_type': ['apartment', 'apartment', 'townhouse', 'townhouse', 'house', 'house', 
                      'apartment', 'apartment', 'townhouse', 'house', 'townhouse', 'house', 
                      'apartment', 'apartment', 'house', 'townhouse', 'apartment', 'apartment', 'house', 'house'],
    'rent': [1200, 1400, 1600, 1800, 2100, 2500, 1100, 1350, 1950, 2400, 1550, 1850, 1150, 1380, 2600, 2000, 1450, 1180, 2200, 2700]
})

# One-hot encode 
prototype_data = pd.get_dummies(prototype_data, columns=['location', 'property_type'])

# Features and target
X = prototype_data[['bedrooms', 'bathrooms', 'sqft', 
                    'location_downtown', 'location_suburb',
                    'property_type_apartment', 'property_type_house', 'property_type_townhouse']]
y = prototype_data['rent']

model = LinearRegression()
model.fit(X, y)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        bedrooms = float(data.get('bedrooms', 0))
        bathrooms = float(data.get('bathrooms', 0))
        sqft = float(data.get('sqft', 0))
        location = data.get('location', 'downtown').lower()
        property_type = data.get('property_type', 'apartment').lower()

        # One-hot encoding manually for API
        location_downtown = 1 if location == 'downtown' else 0
        location_suburb = 1 if location == 'suburb' else 0

        property_apartment = 1 if property_type == 'apartment' else 0
        property_house = 1 if property_type == 'house' else 0
        property_townhouse = 1 if property_type == 'townhouse' else 0

        features = np.array([[bedrooms, bathrooms, sqft,
                              location_downtown, location_suburb,
                              property_apartment, property_house, property_townhouse]])

        prediction = model.predict(features)[0]

        return jsonify({
            'success': True,
            'predicted_rent': round(prediction, 2)
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
